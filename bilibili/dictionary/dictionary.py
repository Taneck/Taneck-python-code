d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)

lst1 = [10,20,39,49]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj)
d=dict(zipobj)
print(d)

d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
d={t:10}
print(d)

#lst=[10,20,30]   字典的键必须是不可变数据类型
#print({lst:10})

d={'hello':10,'world':20,'python':30}
print(d['hello'])
print(d.get('hello'))
#两者有区别
#print(d['java']) 报错
print(d.get('java'))

for item in d.items():
    print(item)
for key,value in d.items():
    print(key,'---->',value)

d={1001:'abc',1002:'via',1003:'sfq'}

d[1004]='gqs'
print(d)
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

values=d.values()
print(values)
print(list(values))
print(tuple(values))

lst=list(d.items())
print(lst)
d=dict(lst)
print(d)

print(d.pop(1001))
print(d)

print(d.popitem())#随机删除
print(d)

d.clear()
print(d)

import random
d={item:random.randint(1,100) for item in range(0,5,2)}
print(d)

lst1=[1001,1002,1003]
lst2=['aaa','bbb','ccc']
d={key:value for key,value in zip(lst1,lst2)}
print(d)

d1={'a':10,'b':20}
d2={'c':30,'d':40}
merged_dict=d1|d2
print(merged_dict)

d1={'a':10,'b':20}
d2={'a':30,'c':40}
merged_dict=d1|d2
print(merged_dict)

fruits=['apple','orange','pear','grape']
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10 apples')
        case 'orange',3:
            print('3 oranges')
        case 'pear',4:
            print('4 pears')
        case 'grape',5:
            print('5 grapes')