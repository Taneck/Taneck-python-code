lst = ['hello', 'world', 23, 14]
print(lst)

lst = list('helloworld')
print(lst)
lst = list(range(1, 10, 2))
print(lst)

del lst

lst = ['hello', 'world', 'python', 'php']
for item in lst:
    print(item)
for i in range(0, len(lst)):
    print(i, '---->', lst[i])
for index, item in enumerate(lst):  # index是序号，不是索引
    print(index, item)
for index, item in enumerate(lst, start=1):
    print(index, item)
for index, item in enumerate(lst, 1):
    print(index, item)

lst = ['hello', 'world', 'python']
print(lst, id(lst))
lst.append('sql')
print(lst, id(lst))

lst.insert(1, 100)
print(lst)
lst.remove('world')
print(lst)
x = lst.pop(1)
print(x)
print(lst)
lst.reverse()
print(lst)
new_list = lst.copy()
print(new_list)
lst.clear()
print(lst, id(lst))

lst = [23, 14, 153, 2351, 213]
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

lst2 = ['Banana', 'apple', 'orange']
lst2.sort(key=str.lower)
print(lst2)

lst = [23, 14, 153, 2351, 213]
print(lst)
new = sorted(lst)
print(new)
print(lst)
new = sorted(lst, reverse=True)
print(new)
print(lst)

llst = [item for item in range(1, 11)]
print(llst)

import random

llst = [random.randint(1, 100) for _ in range(10)]
print(llst)

llst = [i for i in range(10) if i % 2 == 0]
print(llst)

llst=[['a',1,3],['wqe','asf',2]]
print(llst)
for row in llst:
    for item in row:
        print(item,end='\t')
    print()

llst=[[j for j in range(5)] for i in range (4)]
print(llst)