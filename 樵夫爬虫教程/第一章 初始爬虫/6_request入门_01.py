import requests

query =input('请输入一个你喜欢的明星：')
# f + str 的作用是将一个字符塞进一个字符串
url =f'https://www.sogou.com/web?query={query}'

dict = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# header的作用是伪装成浏览器，网址栏里所用的地址一定是get请求方式
resp = requests.get(url,headers=dict)

print(resp.text) #拿到页面源代码

# 关掉请求
resp.close()