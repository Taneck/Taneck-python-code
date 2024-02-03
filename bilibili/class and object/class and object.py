class Person():
    pass


class Cat:
    pass


per1 = Person()
print(type(per1))

print('-' * 50)


class Student:
    school = 'abc'  # 类属性：定义在类中，方法外的变量

    # 初始方法方法
    def __init__(self, xm, age):  # xm，nl是方法的参数，是局部变量，xm，nl的作用域是整个__init__方法
        self.name = xm  # =左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age = age  # 实例的名称和局部变量的名称可以相同

    # 定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫:{self.name},今年:{self.age}岁')

    # 静态方法,不会自带self
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')

    # 类方法
    @classmethod
    def cm(cls):  # 自带一个cls--class的缩写
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')


# 创建类的对象
stu = Student('vae', 18)  # 由于__init__方法中有两个形参，所以创建类的对象时要传两个参数，self是自带的参数，无需传入
# 实例属性，使用对象名进行打点调用
print(stu.name, stu.age)
# 类属性，直接使用类名，打点调用
print(Student.school)
# 实例方法，使用对象名进行打点调用
stu.show()
# 类方法，直接使用类名打点调用
Student.cm()
# 静态方法，直接使用类名打点调用
Student.sm()

print('-' * 50)

stu1 = Student('aaa', 19)
stu2 = Student('bbb', 20)
print(stu1.name, stu1.age)
print(stu2.name, stu2.age)
# 为stu2动态绑定一个实例属性
stu2.gender = '男'
print(stu2.name, stu2.age, stu2.gender)  # 但是stu1不行


# 绑定动态方法
def introduce():
    print('我是一个普通的函数，我被动态绑定成类stu2对象的方法')


stu2.fun1 = introduce
# 调用
stu2.fun1()

print('-' * 50)


class Stustu():
    def __init__(self, name, age, gender):
        self._name = name  # self._name受保护的，只能本类和子类访问
        self.__age = age  # self.__age表示私有的，只能类本身去访问
        self.gender = gender  # 普通的实例属性，类的内部，外部，子类都可以访问

    def _fun1(self):  # 受保护的
        print('子类及本身可以访问')

    def __fun2(self):  # 私有的
        print('只有定义的类可以访问')

    def show(self):  # 普通的实例方法
        self._fun1()  # 类本身访问受保护的方法
        self.__fun2()  # 类本身访问私有的方法
        print(self._name)  # 受保护的实例属性
        print(self.__age)  # 私有的实例属性


stu = Stustu('abc', 20, '男')
print(stu._name)  # 但是stu.__age不行，因为在类的定义之外私有属性不能用；；方法也同理

# 私有实例属性和方法强制访问方式
print(stu._Stustu__age)
stu._Stustu__fun2()

print('-' * 50)


class Stuuuu:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    # 使用@property 修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender

    # 将gender这个属性设置为可写属性
    @gender.setter
    def gender(self, value):
        if value != '男' and value != '女':
            print('性别有误，已将性别默认设置为男')
        else:
            self.__gender = value


stu = Stuuuu('ccc', '男')
print(stu.name, '的性别为', stu.gender)  # stu.gender就会去执行stu.gender()
# 未加setter前，不能修改 stu.gender='女‘

# 加setter后
stu.gender = '其他'
print(stu.name, '的性别为', stu.gender)

print('-' * 50)


# 继承
class Person:  # 默认继承类object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.name},我今年{self.age}岁')


class Son_stu(Person):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)  # 调用父类的初始化方法
        self.stunum = stunum

    def show(self):
        # 调用父类中的方法
        super().show()  # 如果没必要，也可以不调用父类
        print(f'我来自shanghai,我的学号是:{self.stunum}')


class Son_doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


stu = Son_stu('qaq', 20, 1001)
doctor1 = Son_doctor('vae', 18, '医科')

stu.show()
doctor1.show()

print('-' * 50)


# 多继承
class FatherA:
    def __init__(self, name):
        self.name = name

    def showA(self):
        print('父类A中的方法')


class FatherB:
    def __init__(self, age):
        self.age = age

    def showB(self):
        print('父类B中的方法')


class SonOfAAndB(FatherA, FatherB):
    def __init__(self, name, age, gender):
        FatherA.__init__(self, name)  # 有两个父类时不能使用super
        FatherB.__init__(self, age)
        self.gender = gender


son1 = SonOfAAndB('qwe', 20, '女')
son1.showA()
son1.showB()

print('-' * 50)
# 方法重写 在143行中对Son_stu进行方法重写，对比Son_doctor
stu = Son_stu('qaq', 20, 1001)
doctor1 = Son_doctor('vae', 18, '医科')

stu.show()
doctor1.show()
print('-'*50)