def get_sum(num):
    s = 0
    for i in range(1, num + 1):
        s += i
    print('1到{num}之间的累加和为{s}')


get_sum(10)
get_sum(100)
get_sum(500)


def happy_birthday(name, age):
    print('祝' + name + '生日快乐')
    print(str(age) + '岁生日快乐')


happy_birthday('abc', '18')
happy_birthday(age='18', name='abc')
happy_birthday('abc', age=18)  # 只能位置参数在前，关键字参数在后

print('-' * 50)


def happy_birthday111(name='abc', age=18):  # 默认值参数在最后
    print('祝' + name + '生日快乐')
    print(str(age) + '岁生日快乐')


happy_birthday111()
happy_birthday111('qaq')
happy_birthday111(age=19)

print('-' * 50)


def fun(*para):  # 个数可变的位置参数
    print(type(para))
    for item in para:
        print(item)


fun(10)
fun(10, 20, 30, 40)
fun([10, 20, 30, 40])
fun(*[10, 20, 30, 40])  # 在调用时，参数前加一颗星，会将列表进行解包


def fun2(**kwpara):  # 个数可变的关键字参数
    print(type(kwpara))
    for key, value in kwpara.items():
        print(key, '-------->', value)


fun2(name='abc', age=18, height=180)
d = {'name': 'abc', 'age': 18, 'height': 180}
fun2(dic=d)
fun2(**d)

print('-' * 50)


def get_sum(num):
    s = odd_sum = even_sum = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            odd_sum += i
        else:
            even_sum += i
        s += i
    return odd_sum, even_sum, s


result = get_sum(10)
print(type(result))
print(result)

a, b, c = get_sum(10)  # 系列解包赋值
print(a)
print(b)
print(c)

print('-' * 50)


def calc3(x, y):
    global s  # 声明为全局变量
    s = 300  # 声明和赋值必须是分开的
    return s + x + y


print(calc3(10, 20))
print(s)

print('-' * 50)
# 匿名函数
s = lambda a, b: a + b  # 只能使用一次，一般使用于只有一句代码且只有一个返回值
print(type(s))
print(s(10, 20))

print('-' * 50)
student_score = [
    {'name': 'aaa', 'score': 98},
    {'name': 'bbb', 'score': 95},
    {'name': 'ccc', 'score': 100},
    {'name': 'ddd', 'score': 65},
]

student_score.sort(key=lambda x: x.get('score'), reverse=True)  # 倒序
print(student_score)
print('-' * 50)

