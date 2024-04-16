import baostock as bs
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose
from datetime import datetime, timedelta

def stock_price_prediction(stock_code, predict_days):
    #登录baostock
    lg = bs.login()

    #设置日期范围
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d")#分析天数

    #查询股票数据
    rs = bs.query_history_k_data(stock_code,
                                 "date,open,close",
                                 start_date=start_date,
                                 end_date=end_date,
                                 frequency="d",
                                 adjustflag="3")
    data_list = []
    while rs.next():
        data_list.append(rs.get_row_data())
    data = np.array(data_list)

    #数据处理
    close_prices = data[:, 2].astype(float)  #仅使用收盘价
    close_prices_diff = np.diff(close_prices)  #计算价格差分

    #季节性分解
    result = seasonal_decompose(close_prices_diff, model='additive', period=7)
    trend = result.trend
    seasonal = result.seasonal
    residual = result.resid

    #根据季节性分解结果设置SARIMAX参数
    #这里假设季节性周期为7天，根据实际情况调整
    seasonal_order = (1, 1, 1, 7)
    #根据残差选择ARIMA参数
    #这里假设ARIMA参数为(1, 1, 1)，根据实际情况调整
    order = (1, 1, 1)

    # 建立SARIMAX模型
    model = SARIMAX(trend, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=False)

    #预测未来价格变动
    forecast = model_fit.forecast(steps=predict_days)

    #将预测的价格变动转换为未来的收盘价
    future_close_prices = close_prices[-1] + forecast.cumsum()

    #打印预测结果
    print("\n未来%d天的股票价格预测：" % predict_days)
    print("==============================")
    print("|{:^14s}|{:^14s}|".format("日期", "收盘价"))
    print("|" + "-" * 14 + "|" + "-" * 14 + "|")
    for i in range(predict_days):
        date_str = (np.datetime64(end_date) + np.timedelta64(i+1, 'D')).astype(str)
        close_price_str = "%.2f" % future_close_prices[i]
        print("|{:^14s}|{:^14s}|".format(date_str, close_price_str))
    print("==============================")

    #显示历史数据
    display_data(data)

    #退出baostock
    bs.logout()

def display_data(data):
    print("\n获取到的历史股票价格数据：")
    print("=" * 50)
    print("|{:^14s}|{:^14s}|{:^14s}|".format("日期", "开盘价", "收盘价"))
    print("|" + "-" * 14 + "|" + "-" * 14 + "|" + "-" * 14 + "|")
    for row in data:
        print("|{:^14s}|{:^14s}|{:^14s}|".format(row[0], row[1], row[2]))
    print("=" * 50)

#预测的股票代码和天数
stock_code = "sh.601899"  # 贵州茅台
predict_days = 5  # 预测天数
stock_price_prediction(stock_code, predict_days)
print('hello word')