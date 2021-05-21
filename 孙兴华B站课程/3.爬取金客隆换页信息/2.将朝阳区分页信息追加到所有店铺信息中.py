import requests # 获取网页信息
from lxml import etree # 解析网页信息
import pandas as pd

URL = 'https://www.jkl.com.cn/cn/shop.aspx' #注意https和http有区别，我所用的360浏览器为https
UA= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

# 拿取每个城区网址数据。网页上显示为Request Method: GET，所以下面使用get方法，但使用post效果一样
respond_data = requests.get(url=URL,headers=UA).text #因为本节课是获取文字信息，所以加.text

#解析数据
analysis = etree.HTML(respond_data)

city = analysis.xpath('//div[@class="infoLis"]//@href')
print(city)
for i in city:
    city2 = 'https://www.jkl.com.cn/cn/'+i
    respond_data1=requests.get(url=city2,headers=UA).text
    analysis1=etree.HTML(respond_data1)
    store_name = analysis1.xpath('//span[@class="con01"]/text()')
    store_address = analysis1.xpath('//span[@class="con02"]/text()')
    tele_number = analysis1.xpath('//span[@class="con03"]/text()')
    time = analysis1.xpath('//span[@class="con04"]/text()')
    ls = []
    for 店名 in store_name:
        去掉空格后的店名=店名.strip()
        ls.append(去掉空格后的店名)
    数据 = pd.DataFrame({'店名':ls,'地址':store_address,'电话':tele_number,'时间':time})
    数据.to_csv('2.总店铺信息.csv',index=False,header=0,mode='a',encoding='ANSI') # a是追加写模式，每遍历一次，就把一个城区的信息写入csv

    if city2 == 'https://www.jkl.com.cn/cn/shopLis.aspx?id=865':
        for j in range(2, 4):
            换页 = {
                '__EVENTTARGET': 'AspNetPager1',
                '__EVENTARGUMENT': j
            }
            响应数据1 = requests.post(url=city2, headers=UA, data=换页).text  # post的请求，用data传入换页信息；get的请求，有另外的换页传递参数
            解析1 = etree.HTML(响应数据1)
            store_name = 解析1.xpath('//span[@class="con01"]/text()')
            store_address = 解析1.xpath('//span[@class="con02"]/text()')
            tele_number = 解析1.xpath('//span[@class="con03"]/text()')
            time = 解析1.xpath('//span[@class="con04"]/text()')
            ls = []
            for 店名 in store_name:
                去掉空格后的店名 = 店名.strip()
                ls.append(去掉空格后的店名)
            数据 = pd.DataFrame({'店名': ls, '地址': store_address, '电话': tele_number, '时间': time})
            数据.to_csv('2.总店铺信息.csv', index=False, header=0, mode='a',encoding='ANSI')  # a是追加写模式，每遍历一次，就把一个城区的信息写入csv
