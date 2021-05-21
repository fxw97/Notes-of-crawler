# 1.拿到页面源代码
# 2.通过正则表达式re来进一步提取有用信息
import requests
import re
import pandas as pd

for i in range(0,250,25):
    url = f"https://movie.douban.com/top250?start={i}&filter="
    header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    resp = requests.get(url, headers=header)
    html = resp.text
    print(html)
    resp.close()

#解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<comments>.*?)人评价</span>', re.S)

#开始匹配
    result = obj.finditer(html)
    ls = []
    for item in result:
    # print(i.group('name'))
    # print(i.group('year').strip())
    # print(i.group('score'))
    # print(i.group('comments'))
        dic = item.groupdict()
        dic['year'] = dic['year'].strip() #去掉空白区域
        ls.append(dic)
    data = pd.DataFrame(ls)
    data.to_csv("2_4_手刃豆瓣TOP250.csv",index=False,header=None,mode='a',encoding='ANSI')
