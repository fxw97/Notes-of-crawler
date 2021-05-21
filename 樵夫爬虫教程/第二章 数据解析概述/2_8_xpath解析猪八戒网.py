# xpath是在xml文档中搜索内容的一门语言
# html是xml的一个子集
# xpath是靠结点之间的关系去查找内容
import requests
from lxml import etree
import pandas as pd

# 获得HTML源码
url = 'https://guangzhou.zbj.com/search/f/v3512.html?type=new&kw=saas'
resp = requests.get(url)
resp.close()

# print(resp.text)

# 提取解析数据
html = etree.HTML(resp.text)

# 拿到每一个服务商的DIV
divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
del divs[7]  # 实战中发现有空白div，所以在这里去除其对应的div

# 新建空白列表，存数据
a = []; b =[]; c = []; d =[]
for div in divs:
    price = div.xpath('./div/div/a/div[2]/div[1]/span[1]/text()')[0] # xpath语法第一个值是从1开始编号的
    title = 'saas'.join(div.xpath('./div/div/a/div[2]/div[2]/p/text()'))
    com_name = div.xpath('./div/div/a[2]/div/p/text()')[0]
    location = div.xpath('./div/div/a[2]/div/div/span/text()')[0]
    a.append(price)
    b.append(title)
    c.append(com_name)
    d.append(location)

data =pd.DataFrame({'price':a,'title':b,'company_name':c,'location':d})
data.to_csv('2_8_xpath解析猪八戒网.csv',index=False)
print(data.info())