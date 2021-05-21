import requests
from lxml import etree # 解析网页信息
import pandas as pd

URL2 = 'https://www.jkl.com.cn/cn/shopLis.aspx?id=865'
UA2= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

for i in range(1,4):
    换页={
        '__EVENTTARGET': 'AspNetPager1',
        '__EVENTARGUMENT': i
    }
    响应数据1 = requests.post(url=URL2,headers=UA2,data=换页).text # post的请求，用data传入换页信息；get的请求，有另外的换页传递参数
    解析1=etree.HTML(响应数据1)
    store_name = 解析1.xpath('//span[@class="con01"]/text()')
    store_address = 解析1.xpath('//span[@class="con02"]/text()')
    tele_number = 解析1.xpath('//span[@class="con03"]/text()')
    time = 解析1.xpath('//span[@class="con04"]/text()')
    ls = []
    for 店名 in store_name:
        去掉空格后的店名=店名.strip()
        ls.append(去掉空格后的店名)
    数据 = pd.DataFrame({'店名':ls,'地址':store_address,'电话':tele_number,'时间':time})
    数据.to_csv('1.店铺信息—朝阳区(无指定编码).csv',index=False,header=None,mode='a') # a是追加写模式，每遍历一次，就把一个城区的信息写入csv