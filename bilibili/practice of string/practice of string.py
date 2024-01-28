lst = ['京A12345', '沪A23516', '浙A87219']
for item in lst:
    print(item, '的归属地为', item[0:1])

s = 'Helloworld,hellopython,hellojava'
word = input('请输入要查找的字母，请大写输入，查找不区分大小写：')
print('{0}在{1}中一共出现了{2}次'.format(word, s, s.upper().count(word)))
print('-'*50)

lst = [['01', 'fan', 'midea', '800'], ['02', 'washer', 'TCL', '1000'], ['03', 'microwave', 'boss', '500']]
print('code'.ljust(8)+'\t\t'+'type'.ljust(8)+'\t\t'+'brand'.ljust(8)+'\t\t'+'price'.ljust(8)+'\t\t')
for item in lst:
    for i in item:
        print(i.ljust(8),end='\t\t')
    print()

for item in lst:
    item[0]='0000'+item[0]
    item[3]='$'+item[3]
print('code'.ljust(8)+'\t\t'+'type'.ljust(8)+'\t\t'+'brand'.ljust(8)+'\t\t'+'price'.ljust(8)+'\t\t')
for item in lst:
    for i in item:
        print(i.ljust(8),end='\t\t')
    print()