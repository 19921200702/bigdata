import requests
from bs4 import BeautifulSoup
def search_baidu(keyword):
    if not keyword:
        return {"error": "未提供搜索内容"}
    search_url = "http://www.baidu.com/s"
    params = {'wd': keyword}
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        zongjie = soup.find('p', class_='cu-line-clamp-4').get_text().strip() if soup.find('p', class_='cu-line-clamp-4') else ""
        search_results = []
        for result in soup.find_all('h3'):
            title = result.get_text().strip()
            link = result.find('a', href=True)['href'] if result.find('a', href=True) else ""
            search_results.append({
                "summary":zongjie,
                "title": title,
                "url": link
            })
        return search_results
    else:
        return {"error": "搜索失败"}
#coze插件类，不用可以删除
def handler(args) -> str:
    print(args)
    name = args.input.keyword
    result = search_baidu(name)
    return result
#搜索
print(search_baidu("人为什么活着"))