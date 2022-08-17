# 这个发布订阅（观察者）模式学学思路就行了，看完会觉得很巧妙，但是在一个大系统里还是乖乖的
# 用数据库存订阅者发布者信息吧，因为这个设计模式的实现太依赖observers列表了，
# 也就是说会非常占内存，想想一个网站有了几万用户，那个时候内存大概率爆炸
"""
内容:
定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时,所有依赖于它的对象
都得到通知并被自动更新。观察者模式又称“发布-订阅”模式

角色:
抽象主题(Subject)
具体主题(ConcreteSubject)——发布者
抽象观察者(Observer)
具体观察者(ConcreteObserver)——订阅者

适用场景:
当一个抽象模型有两方面，其中一个方面依赖于另一个方面。将这两者封装在独立对象中以使它们可以各自独立地改变和复用。
当对一个对象的改变需要同时改变其它对象，而不知道具体有多少对象有待改变。
当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之，你不希望这些对象是紧密耦合的。

"""

from abc import ABCMeta, abstractmethod


# 抽象订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self, notice):  # notice是一个Notice类的对象
        pass


# 抽象发布者
class Notice(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def attach(self, obs):
        pass

    @abstractmethod
    def detach(self, obs):
        pass

    @abstractmethod
    def company_info(self, info):
        pass


# 具体发布者
class StaffNotice(Notice):
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def company_info(self, info):
        for obs in self.observers:
            obs.update(info)  # 发布者调用订阅者内的方法，订阅者索取消息


# 具体订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice


notice = StaffNotice()
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)

print(s1.company_info, s2.company_info)

notice.company_info(111)
print(s1.company_info, s2.company_info)

notice.detach(s2)
notice.company_info(222)
print(s1.company_info, s2.company_info)
"""
优点︰
目标和观察者之间的抽象耦合最小
支持广播通信"""

# 原始复杂版，学一下python基础用法还是可以的
"""
class Observer(metaclass=ABCMeta):  # 抽象订阅者
    @abstractmethod
    def update(self, notice):  # notice是一个Notice类的对象
        pass


class Notice():  # 抽象发布者
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)  # 发布者调用订阅者内的方法，订阅者索取消息


class StaffNotice(Notice):  # 具体发布者
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# obj = StaffNotice("abc")
# obj.company_info = "xyz"
# print(obj.company_info)

notice = StaffNotice("初始信息，传不传都可以，我指定了false做默认值")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司今年业绩非常好，给大家发奖金!!!"
print(s1.company_info)"""
