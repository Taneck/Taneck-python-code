class Person:
    def eat(self):
        print('人吃五谷杂粮')


class Cat:
    def eat(self):
        print('猫喜欢吃鱼')


class Dog:
    def eat(self):
        print('狗喜欢啃骨头')


# 三个类中都有一个同名的方法eat
# 编写函数
def fun(obj):
    obj.eat()


per = Person()
cat = Cat()
dog = Dog()

fun(per)  # python中的多态，不关心对象的数据类型，只关心对象是否具有同名方法
fun(cat)
fun(dog)
