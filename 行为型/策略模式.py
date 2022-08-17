"""
内容:
定义一系列的算法，把它们一个个封装起来，并且使它们可相互替换。
本模式使得算法可独立于使用它的客户而变化。

角色:
抽象策略(Strategy)
具体策略(ConcreteStrategy)
上下文(Context)

在不同的时候切换策略很关键
使用场景：
假设你在设计一个打车软件，有两种算法，一种是最好的算法但是慢，一种是不好的算法但是快,那么你就需要
针对打车这个场景，为这两种算法设计＂如何切换，切换的条件是什么＂等




"""

from abc import ABCMeta, abstractmethod


# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


# 具体策略
class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)


# 具体策略
class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


# 上下文
class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):  # 允许你后期更改策略
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)

data = "［假设这里就是你要处理的数据］"
s1= FastStrategy()
s2 = SlowStrategy()
context = Context(s1,data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()


"""
优点:
定义了一系列可重用的算法和行为消除了一些条件语句
可以提供相同行为的不同实现

缺点:
客户必须了解不同的策略
"""