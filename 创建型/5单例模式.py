"""
内容:保证一个类只有一个实例，并提供一个访问它的全局访问点。

角色:
单例(Singleton)

优点∶
对唯一实例的受控访问,单例相当于全局变量，但防止了命名空间被污染"""


class Singleton(object):  # object默认不写
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):  # 看Singleton类本身有没有_instance属性或者方法
            cls._instance = super(Singleton, cls).__new__(cls)  # 调用object总类中的生成实例对象方法
        return cls._instance  # 返回生成的实例对象


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)
print(id(a),id(b))#MyClass实例只有一个，但是可以不停修改里面的属性如self.a
