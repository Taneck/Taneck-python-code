try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入另一个整数：'))
    result = num1 / num2
    print('结果:', result)
except ZeroDivisionError:
    print('除数为0')
except ValueError:
    print('不能将字符串转成整数')
except BaseException:
    print('未知异常')
else:  # 无异常时才会执行
    print('无异常')
finally:  # 无论如何都会执行
    print('程序结束')
print('-' * 50)

try:
    gender = input('请输入你的性别：')
    if gender != '男' and gender != '女':
        raise Exception('性别只能是男或者女')
    else:
        print('您的性别是：', gender)
except Exception as e:
    print(e)

i = 1
j = 0
while 1 < 10:
    print(i)
    i += 1
