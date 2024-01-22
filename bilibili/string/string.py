s1 = 'Hello world'
s2 = s1.lower()
s3 = s1.upper()
print(s1, s2, s3)
e_mail = 'abc@qq.com'
lst = e_mail.split('@')
print(lst[0], '和', lst[1])

print(s1.count('ell'))

print(s1.find('o'))
print(s1.find('p'))

print(s1.index('o'))
# print(s1.index('p'))    会报错

print('demo.py'.endswith('.py'))
print(s1.startswith('H'))

s2 = s1.replace('o', '你好')
print(s2)

s2 = s1.replace('o', '你好', 1)
print(s2)

print(s1.center(20))
print(s1.center(20, '*'))

s = '    hello     world'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = 'dl-helloworld'
print(s.strip('ld'))
print(s.lstrip('ld'))
print(s.rstrip('ld'))

name = '啦啦啦'
age = 19
score = 98.5
print('姓名为%s,年龄:%d,成绩:%.1f' % (name, age, score))
print(f'姓名为{name},年龄:{age},成绩:{score}')
print('姓名为{0},年龄:{1},成绩:{2}'.format(name, age, score))
print('姓名为{2},年龄:{0},成绩:{1}'.format(age, score, name))

s = 'helloworld'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))
print(s.center(20, '*'))

print('{0:,}'.format(984214124))
print('{0:,}'.format(984214124.3164314))
print('{0:.2f}'.format(984214124.3164314))
print('{0:.5}'.format('helloworld'))

a = 425
print('{0:b},{0:d},{0:o},{0:x},{0:X}'.format(a))
b = 3.1415926
print('{0:.2f},{0:.2E},{0:.2e}.{0:.2%}'.format(b))

s = '我想学编程'
scode = s.encode()  # 默认为utf-8,中文占三个字节
print(scode)

scode_gbk = s.encode('gbk', errors='replace')  # gbk中文占两个字节
print(scode_gbk)

s2='✌️'
scode_ignore=s2.encode('gbk','ignore')
print(scode_ignore)
#scode_strict=s2.encode('gbk','strict')  strict会报错
#print((scode_strict))
scode_replace=s2.encode('gbk','replace')
print(scode_replace)

print(bytes.decode(scode_gbk,'gbk'))
print(scode_gbk.decode('gbk'))


print('123'.isdigit())
print('一二三'.isdigit())
print('0b1010'.isdigit())
print('壹'.isdigit())
print('ⅠⅡⅢⅣ'.isdigit())

print('123'.isnumeric())
print('一二三'.isnumeric())
print('0b1010'.isnumeric())
print('壹'.isnumeric())
print('ⅠⅡⅢⅣ'.isnumeric())

print('')