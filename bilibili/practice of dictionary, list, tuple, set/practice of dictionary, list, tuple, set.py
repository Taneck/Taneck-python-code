dict_ticket={'G1234':['aaa to bbb','10:00'],'G4213':['cqc to vdw','12:20']}
print('车次       出发地 to 到达地      发车时间')
for key in dict_ticket.keys():
    print(key,end='         ')
    for item in dict_ticket.get(key):
        print(item,end='        ')
    print()
train_number=input('请输入要购买的车次')
info=dict_ticket.get(train_number,'不存在')
if info != '不存在':
    person=input('请输入乘车人')
    s=info[0]+'  '+info[1]
    print('您已购买了'+train_number+' '+'乘车人为 '+person+'车辆信息为 '+s)
else:
    print('输入的车次有误')

s=set()
for i in range(1,3):
    info=input(f'请输入第{i}位好友的姓名和手机号')
    s.add(info)
for item in s:
    print(item)