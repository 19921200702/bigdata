import logging
import inspect



class CustomLogger:
    def __init__(self, name="CustomLogger"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # 设置日志的最低级别为DEBUG

        # 创建控制台日志处理器
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义日志格式，包含时间、进程ID、线程ID、文件名、函数名、代码行、日志级别和日志消息
        formatter = logging.Formatter(
            '%(asctime)s - PID:%(process)d - TID:%(thread)d - %(custom_filename)s - %(custom_funcName)s - Line:%(custom_lineno)d - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

    def debug(self, message):
        frame = inspect.currentframe().f_back
        self._log(logging.DEBUG, message, frame)

    def info(self, message):
        frame = inspect.currentframe().f_back
        self._log(logging.INFO, message, frame)

    def warning(self, message):
        frame = inspect.currentframe().f_back
        self._log(logging.WARNING, message, frame)

    def error(self, message):
        frame = inspect.currentframe().f_back
        self._log(logging.ERROR, message, frame)

    def _log(self, level, message, frame):
        file_name = frame.f_code.co_filename
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno


        extra_info = {
            'custom_filename': file_name,
            'custom_funcName': function_name,
            'custom_lineno': line_no
        }

        self.logger.log(level, message, extra=extra_info)


# 测试自定义日志
if __name__ == '__main__':
    logger = CustomLogger()

    # 测试不同的日志级别
    logger.debug("这是一条调试信息")
    logger.info("这是一条普通信息")
    logger.warning("这是一条警告信息")
    logger.error("这是一条错误信息")