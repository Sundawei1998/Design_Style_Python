"""
内容:将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。

两种实现方式类适配器:
使用多继承对象适配器
使用组合

角色:
目标接口(Target)
待适配的类(Adaptee)
适配器(Adapter)

适用场景:
你在开发一个老系统，此时领导交代给你一个新的系统让你融合丰富功能，你发现新系统的命名风格
跟老系统的不一样，但是你又想要把新系统的代码复用到老系统，如果一个一个改新系统命名风格，
麻烦不说还容易犯错，那么此时你就可以用适配器模式，让老系统延续之前的风格，并直接引用新系统代码"""

import abc

"""－－－－－老系统－－－－－"""


class Abs_Prod(metaclass=abc.ABCMeta):  # 抽象产品
    @abc.abstractmethod
    def pay(self):
        pass


class Ali_Pay(Abs_Prod):
    def pay(self):
        print("选用阿里支付")


"""－－－－－新系统－－－－－"""


class Bank_Pay():
    def cost(self):
        print("选用银行支付")


# 显然，老系统习惯用pay方法，新系统习惯cost方法，必须融合

# 类的继承
class New_Bank_Pay1(Abs_Prod, Bank_Pay):
    def pay(self):
        self.cost()


# 组合
class New_Bank_Pay2(Abs_Prod):
    def __init__(self, payment):
        self.a = payment

    def pay(self):
        self.a.cost()


res = Ali_Pay().pay()
res = New_Bank_Pay1().pay()

a = Bank_Pay()
b = New_Bank_Pay2(a).pay()