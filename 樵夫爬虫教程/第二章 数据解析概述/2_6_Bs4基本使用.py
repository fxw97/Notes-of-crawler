import requests
from bs4 import BeautifulSoup
import pandas as pd

# 整体思路
# 1.拿到页面源代码
# 2.使用bs4进行解析，拿到数据
c0=[]; c1=[]; c2=[]; c3=[]; c4=[]; c5=[]; c6=[]

for i in range(0,35): # 用于网页分页的大循环
    url = f'http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml'
    resp = requests.get(url)
    resp.close()
    # print(resp.text)

# 2.解析数据
# 2.1 把页面源代码交给BeautifulSoup进行处理，生成bs对象
    page = BeautifulSoup(resp.text,'html.parser') # 'html.parser'作用是指定为html解析器

# 2.2 从bs对象中查找一个或多个数据:find(标签，属性=值)和find_all(标签，属性=值)
# table = page.find('table',class_='hq_table') #因为class是python的关键字，所以在bs4中用class_来作为关键字
    table = page.find('table',attrs={'class':'hq_table'}) # 和上一行代码效果相同，此时可以避免class冲突
# print(table)

# 拿到所有的行数据
    trs = table.find_all('tr')[1:] # tr是行，td是列
    for tr in trs:
        tds = tr.find_all('td') # 拿到每行中所有的td
        c0.append(tds[0].text.strip()) # .text 表示拿到被标签标记的内容
        c1.append(tds[1].text.strip()) # .text 表示拿到被标签标记的内容
        c2.append(tds[2].text.strip()) # .text 表示拿到被标签标记的内容
        c3.append(tds[3].text.strip()) # .text 表示拿到被标签标记的内容
        c4.append(tds[4].text.strip()) # .text 表示拿到被标签标记的内容
        c5.append(tds[5].text.strip()) # .text 表示拿到被标签标记的内容
        c6.append(tds[6].text.strip()) # .text 表示拿到被标签标记的内容

data =pd.DataFrame({'name':c0,'lowest price':c1,'average price':c2,'highest price':c3,'specification':c4,'unit':c5,'date':c6})
data.to_excel('2_6菜价2021-05-19.xlsx')
print('over!!')