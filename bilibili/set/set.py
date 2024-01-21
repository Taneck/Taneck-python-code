s={10,20,30,40}
print(s)

#集合只能存储不可变数据类型
#s={[10,20],[20,30]}

s=set()
print(s)
s={}
print(s,type(s))

s=set('helloworld')
print(s)

s=set([10,20,30])
print(s)

s=set(range(1,10))
print(s)

print(9 in s)
print(max(s))


a={10,20,30,40,50}
b={30,50,88,76,20}
print(a&b)
print(a|b)
print(a-b)
print(a^b)

a.add(100)
print(a)
a.remove(20)
print(a)
a.clear()
print(a)

for item in b:
    print(item)

for index,item in enumerate(b,start=2):
    print(index,'----->',item)

s={i for i in range(1,10)}
print(s)
s={i for i in range(1,10) if i%2==1}
print(s)