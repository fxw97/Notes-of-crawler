import re

# findall:匹配字符串中所有的符合正则的内容
list = re.findall(r'\d+',"我的电话号码是16620188427,中国移动的电话号码是10086")
print("findall",list)

# finditer:匹配字符串中所有的内容，返回的是迭代器(iterator对象)，从迭代器中拿到内容需要.group()
it = re.finditer(r'\d+',"我的电话号码是16620188427,中国移动的电话号码是10086")
list=[]
for i in it:
    list.append(i.group())
print("finditer",list)

# search返回结果是match对象，拿数据需要用.group(),但找到一个结果就会返回
s = re.search(r'\d+',"我的电话号码是16620188427,中国移动的电话号码是10086")
print("search",s.group())

# match是从头开始匹配,因为这里开头不是数字所以会报错
# list2 = re.match(r'\d+',"我的电话号码是16620188427,中国移动的电话号码是10086")
# print("match",list2.group())

# 预加载正则表达式
obj1 = re.compile(r"\d+")

ret = obj1.finditer("我的电话号码是16620188427,中国移动的电话号码是10086")
for it in ret:
    print(it.group())

# (?P<分组名字>正则)可以单独把正则匹配的内容中提取到 分组名字 中，从而进一步提取内容
s ="""
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>大胡子</span></div>
"""
obj2 = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<actor>.*?)</span></div>", re.S) # re.S的作用是能让.匹配换行符

result = obj2.finditer(s)
for m in result:
    print(m.group('id'))
    print(m.group('actor'))