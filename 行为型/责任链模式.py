"""
内容:使多个对象都有机会处理请求,从而避免请求的发送者和接收者之间的耦合关系。
将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

角色:
抽象处理者(Handler)
具体处理者(ConcreteHandler)
客户端(Client)

适用场景:
有多个对象可以处理一个请求，哪个对象处理由运行时决定
在不明确接收者的情况下，向多个对象中的一个提交一个请求

"""

from abc import ABCMeta, abstractmethod

# 抽象处理者
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass

# 具体处理者
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" % day)
        else:
            print("你还是辞职吧")

# 具体处理者
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%s天" % day)
        else:
            print("部门经理职权不足")
            self.next.handle_leave(day)

# 具体处理者
class ProiectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目主管准假%d天" % day)
        else:
            print("项目主管职权不足")
            self.next.handle_leave(day)

a = ProiectDirector()
a.handle_leave(10)

"""
优点︰
降低耦合度:一个对象无需知道是其他哪—个对象处理其请求（中间件也是这样交替处理请求的吧）"""