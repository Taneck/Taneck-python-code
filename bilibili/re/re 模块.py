#
# import regex
#
# pattern = '\\d\\.\\d+'  # 模式字符串 \d十进制数字 \.转义字符相当于. \d+ 0-9数字出现一次或者多次
# s = 'i study python 3.12 every day'
# match = regex.match(pattern, s)  # re.I忽略大小写
# print(match)
# s = '3.12 i study python every day'
# match = regex.match(pattern, s)
# print(match)

import re

pattern = r'\d\.\d+'
s = 'i study python 3.12 every day'
match = re.match(pattern, s)  # match 从头开始
print(match)

s = '3.12 i study python every day'
match = re.match(pattern, s)
print(match)
print(match.start())
print(match.end())
print(match.span())
print(match.string)
print(match.group())

s = 'i study python 3.12 and 3.13 every day'

match = re.search(pattern, s)
print(match)
print('-' * 50)
s1 = 'i study python 3.12 and 3.13 every day'
s2 = '3.12 i study python every day'
s3 = 'i study python every day'

lst1 = re.findall(pattern, s1)
lst2 = re.findall(pattern, s2)
lst3 = re.findall(pattern, s3)
print(lst1)
print(lst2)
print(lst3)
print('-' * 50)

pattern = '黑客|破解|反爬'
s = '我想学习python，想破解一些VIP视频，python可以实现无底线反爬吗'
new_s = re.sub(pattern, 'xxx', s)
print(new_s)
print('-' * 50)

s = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=vscode和vs优劣&fenlei=256'
pattern = '[&|?]'
lst=re.split(pattern,s)
print(lst)