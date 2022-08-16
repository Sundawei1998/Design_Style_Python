"""
内容:内容:定义一个工厂类接口，让工厂子类来创建一系列相关或相互依赖的对象。

角色:
抽象工厂角色
具体工厂角色
抽象产品角色
具体产品角色
客户端


使用场景
生产一部手机，需要手机壳、CPU、操作系统三类对象进行组装，其中每类对象都有不同的种类。对每个具体工厂，分别生产
一部手机所需要的三个对象。相比工厂方法模式，抽象工厂模式中的每个具体工厂都生产多个产品。
"""
import abc


# 抽象工厂
class AbsPhone_Factory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Make_Cpu(self):
        pass

    @abc.abstractmethod
    def Make_System(self):
        pass

    @abc.abstractmethod
    def Make_Shell(self):
        pass


# 抽象产品
class AbsPhone_Cpu(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Cpu(self):
        pass


class AbsPhone_System(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def System(self):
        pass


class AbsPhone_Shell(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Shell(self):
        pass


# 具体产品
class Iphone_Cpu(AbsPhone_Cpu):
    def Cpu(self):
        print("Iphone_cpu")


class Android_Cpu(AbsPhone_Cpu):
    def Cpu(self):
        print("Android_cpu")


class Iphone_System(AbsPhone_System):
    def System(self):
        print("Iphone_system")


class Android_System(AbsPhone_System):
    def System(self):
        print("Android_system")


class Iphone_Shell(AbsPhone_Shell):
    def Shell(self):
        print("Iphone_shell")


class Android_Shell(AbsPhone_Shell):
    def Shell(self):
        print("Android_shell")


# 具体工厂
class Iphone_Factory(AbsPhone_Factory):

    def Make_Cpu(self):
        return Iphone_Cpu()

    def Make_System(self):
        return Iphone_System()

    def Make_Shell(self):
        return Iphone_Shell()

    def make_Phone(self):
        print("手机整体信息：")
        self.Make_Cpu().Cpu()
        self.Make_System().System()
        self.Make_Shell().Shell()


a = Iphone_Factory()
a.make_Phone()

"""优点:
将客户端与类的具体实现相分离
每个工厂创建了一个完整的产品系列,使得易于交换产品系列
有利于产品的一致性(即产品之间的约束关系)当类之间使用需要特定类搭配时

缺点:
难以支持新种类的(抽象)产品
"""