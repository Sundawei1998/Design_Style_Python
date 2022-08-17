"""
内容:
定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法
使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

角色:
抽象类(AbstractClass):定义抽象的原子操作(钩子操作);实现一个模板方法作为算法的骨架。
具体类(ConcreteClass)︰实现原子操作

适用场景:
—次性实现一个算法的不变的部分
各个子类中的公共行为应该被提取出来并集中到一个公共父类中以
避免代码重复.(抽象类中的run)
控制子类扩展

这像不像实际开发或者说你写为代码的样子
"""
from abc import ABCMeta, abstractmethod
from time import sleep

# 抽象类
class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # 模板方法
    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(5)
            except KeyboardInterrupt:
                break
        self.stop()

# 具体类
class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口结束运行")

    def repaint(self, ):
        print(self.msg)


MyWindow("kk").run()
