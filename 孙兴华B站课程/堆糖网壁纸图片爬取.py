# 流程
# 分析网站
# 目标：爬取图片
# 1.关键字：二次元
# https://www.duitang.com/search/?kw=%E6%8F%92%E7%94%BB%E5%A3%81%E7%BA%B8&type=feed
# 数据加载方式 瀑布流加载为24
# https://www.duitang.com/napi/blog/list/by_search/?kw=%E4%BA%8C%E6%AC%A1%E5%85%83&start=24

import urllib.parse
import requests
import json
import jsonpath

# 关键字转义
kw = '手绘壁纸'
kw = urllib.parse.quote(kw)
n = 1

for index in range(0,240,24):
    # 1.目标网址
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'.format(kw,index)

    # 2.模拟浏览器发送请求，并接收响应
    resp = requests.get(url)
    web_data = resp.text

    # 3.解析网络内容，提取数据
    html = json.loads(web_data)
    photos = jsonpath.jsonpath(html,'$..path')  # 从文件根目录开始往上找，找到所有path对应的文件

    # 4.将文件导出保存

    for i in photos:
        response = requests.get(i)
        with open(r"C:\Users\A\Desktop\wallpaper\{}.jpg".format(n),'wb') as f: # wb代表二进制的写入
            f.write(response.content) # 图片一定要保存为content二进制流
        n += 1