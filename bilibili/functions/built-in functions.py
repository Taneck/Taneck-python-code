# 类型转换函数
# bool(),str(),int(),float(),list(),tuple(),set()

# 数学函数
print(abs(-3))
print(divmod(10, 3))
print(max([3, 4, 15, 12, 3]))
print(max('hello'))
print(min([3, 4, 15, 12, 3]))
print(pow(3, 4))
print(round(3.1415926, 4))
print(round(31415.926, -1))
print(sum([10, 24, 35]))

# 迭代器操作函数
lst = [54, 56, 77, 4, 56, 34]
asc_lst = sorted(lst)
desc_lst = sorted(lst, reverse=True)
print(asc_lst)
print(desc_lst)

rev_lst = reversed(lst)
print(type(rev_lst))
print(list(rev_lst))

x = ['a', 'b', 'c', 'd']
y = [10, 20, 30, 40, 50]
zip_obj = zip(x, y)
print(type(zip_obj))
print(list(zip_obj))

enum = enumerate(y, start=1)
print(type(enum))
print(tuple(enum))

lst2 = [10, 20, '', 30]
print(all(lst))
print(all(lst2))

lst3 = [0, '', None]
print(any(lst2))
print(any(lst3))

x = ['a', 'b', 'c', 'd']
y = [10, 20, 30, 40, 50]
zip_obj = zip(x, y)
print(next(zip_obj))
print(next(zip_obj))
print(next(zip_obj))


def fun(num):
    return num % 2 == 1


obj = filter(fun, range(10))
print(type(obj))
print(list(obj))


def upper(x):
    return x.upper()


lst3 = ['hello', 'world', 'python']
obj = map(upper, lst3)
print(type(obj))
print(list(obj))

# 其他函数
# len(),id(),type(),eval()
print(format(3.14, '20'))  # 数值默认右对齐
print(format('hello', '20'))  # 字符串默认左对齐
print(format(3.14, '<20'))
print(format('hello', '#>20'))
print(format('hello', '#^20'))

print(format(3.1415926, '.2f'))
print(format(20, 'b'))
print(format(20, 'o'))
print(format(20, 'x'))
print(format(20, 'X'))
