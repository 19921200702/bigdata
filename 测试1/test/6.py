import requests
import json

json = json.loads(requests.get("https://api.rebang.today/v1/items?tab=zhihu&date_type=now&version=1",
                               headers={"User-Agent": "Mozilla/5.0"}).json()["data"]["list"])
for j in json:
    print(j["title"], "\n", j["www_url"], "\n***\n")
