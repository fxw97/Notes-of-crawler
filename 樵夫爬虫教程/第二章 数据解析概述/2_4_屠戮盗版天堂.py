# 1.定位到2020必看片
# 2.从2020必看片中提取到子页面链接地址
# 3.请求子页面链接地址，拿到我们想要的下载地址
import requests
import re
import pandas as pd

domain = "https://www.dytt89.com/"
resp = requests.get(domain,verify=False) # verify=False去掉安全验证
resp.close()
resp.encoding = 'gb2312' #指定字符集，用于解乱码，gb2312是从网页text中找到的charset=gb2312
# print(resp.text)

# 定位到所需网页源代码区域
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S) # 注意这里?容易打成中文状态下的？，是不对的

#
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)"', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')

    # 提取子页面链接
    result2 = obj2.finditer(ul)
    for iit in result2:
        # 拼接子页面地址：域名+子页面地址
        child_href = domain + iit.group('href').strip('/')
        child_href_list.append(child_href) #把子页面保存起来

# 提取子页面内容
movie = []
download =[]
for herf in child_href_list:
    child_resp = requests.get(herf,verify=False)
    child_resp.encoding = 'gb2312'
    result3 =obj3.search(child_resp.text)
    movie.append(result3.group('movie'))
    download.append(result3.group('download'))

# 保存数据
data = pd.DataFrame({'Movie':movie,'Download':download})
data.to_excel('2_4_屠戮盗版天堂.xlsx',index=False,encoding='ANSI')