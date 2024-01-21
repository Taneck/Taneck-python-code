t = ('abc', [12, 23, 41], 'python')
print(t)

t = tuple('helloworld')

print(t)

t = tuple([10, 20, 30, 40])
print(t)

t = (11)
print(t, type(t))
t = (11,)
print(t, type(t))

y = (i for i in range(1, 4))
print(y)  # 生成器对象
print(y.__next__())
print(y.__next__())
print(y.__next__())

t = tuple(y)
print(t)
