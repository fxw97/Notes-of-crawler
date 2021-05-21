# 爬虫：通过编写程序来获取到互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容
# python搞定以上需求特别简单
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)

with open("3_my baidu.html",mode="w",encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8')) #将读取到网页的页面源代码写入html文件中
print("over!")
f.close()