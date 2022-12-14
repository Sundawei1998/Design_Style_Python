import abc

"""当你想确保新的类重写某些方法时，或者说某些类之间都必须要有某写方法时．
"""


class Payment(metaclass=abc.ABCMeta):  # 改变元类，继承新的元类，新的元类里面才有这个装饰器
    @abc.abstractmethod  # 实例化的时候这个方法无法被实例化，因此继承了这个类的方法被实例化的时候就
    # 需要重写pay方法，代表这是个抽象化类，只能继承无法实例化．
    def pay(self, money):
        print(money)
        pass


class Alipay(Payment):
    def pay(self, money):
        print(money)

    pass


a = Alipay()
a.pay(100)

"""面向对象设计SOLID原则
开放封闭原则:一个软件实体如类、模块和函数应该对扩展开放，对修改关闭。即软件实体应尽量在不修改原有代码的情况下进行扩展。
里氏替换原则:所有引用父类的地方必须能透明地使用其子类的对象。
依赖倒置原则:高层模块不应该依赖低层模块二者都应该依赖其抽象;抽象不应该依赖细节;细节应该依赖抽象。换言之，要针对接口编程，而不是针对实现编程。
接口隔离原则:使用多个专门的接口，而不使用单一的总接口，即客户端不应该依赖那些它不需要的接口。
单一职责原则:不要存在多于一个导致类变更的原因。通俗的说，即一个类只负责一项职责。"""
