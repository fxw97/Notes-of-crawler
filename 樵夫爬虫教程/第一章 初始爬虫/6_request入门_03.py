import requests

#原始地址：
url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20"

#重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action":"",
    "start": 0,
   " limit": 20
}

# 新地址（相当于封装了网址？之后的一些特征参数）：
url1 = "https://movie.douban.com/j/chart/top_list"

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

resp = requests.get(url1, params=param,headers=headers)

print(resp.json())

# 关掉请求
resp.close()