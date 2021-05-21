# 拿到主页面的源代码，然后提取到子页面的链接地址，href
# 通过href拿到子页面的内容，从子页面中找到图片的下载地址 img -> src
# 下载图片
import requests
from bs4 import BeautifulSoup
import time

m=0
for i in ['']+['_{}'.format(i) for i in range(2,3)]:
    url = f'https://www.umei.net/bizhitupian/diannaobizhi/index{i}.htm'
    resp = requests.get(url)
    resp.encoding = 'utf-8' #处理乱码
    resp.close()


# 把源代码交给bs4
    main_page = BeautifulSoup(resp.text,'html.parser')
    a_list = main_page.find('div',class_="TypeList").find_all('a')  # 把范围逐渐缩小
    for a in a_list:
        href = a.get('href')
        # 拿到子页面的源代码
        chlid_page_resp = requests.get('https://www.umei.net' + href)
        chlid_page_resp.encoding='utf-8'
        chlid_page_text = chlid_page_resp.text
        # 从子页面拿到图片的下载途径
        child_page = BeautifulSoup(chlid_page_text,'html.parser')
        p = child_page.find('p',align="center")
        img = p.find('img') # 得到的为 <img src="http://kr.shanghai-jiuxin.com/file/2020/0807/f1fdba29810f449bc5b339f8b401f845.jpg"/>
        src = img.get('src') # 进一步得到图片的src下载路径
        # 下载图片
        img_resp = requests.get(src)
        m+=1
        img_name = f'{m}.jpg'
        with open('F:/BaiduNetdiskDownload/img/'+ img_name,mode='wb') as f:
            f.write(img_resp.content) # img_resp.content 这里拿到的是字节，需要进一步写入到jpg文件中形成图片
        print('over!',img_name)
        time.sleep(1) # 下载一张图片休息一秒，以防被封ip

print('all over')