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
match = re.match(pattern, s)
print(match)

s = '3.12 i study python every day'
match = re.match(pattern, s)
print(match)