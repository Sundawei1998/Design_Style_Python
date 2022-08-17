"""
内容:定义一个用于创建对象的接口(工厂接口)，让子类决定实例化哪一个产品类。

角色:
抽象工厂角色(Creator)
具体工厂角色(Concrete Creator)抽象产品角色 (Product)
具体产品角色(Concrete Product)

使用场景:
当你创建某个类需要往里面传入很多参数，但是你又不想让客户这么麻烦去输入那些参数，
你就可以用简单工厂模式，帮他完善这些需要输入的信息，帮他创建这个类．
而简单工厂是用一个工厂控制许多产品，当你新增加产品的时候就需要修改唯一工厂代码，所以
最好能分开成许多的小工厂
"""
import abc


class PaymentFactory(metaclass=abc.ABCMeta):  # 抽象工厂
    @abc.abstractmethod
    def create_payment(self):
        pass


class Ali_Factory(PaymentFactory):  # 具体工厂
    def create_payment(self):
        return Ali_Prod()


class QQ_Factory(PaymentFactory):  # 具体工厂
    def create_payment(self):
        return QQ_Prod()


class HuaBei_Factory(PaymentFactory):  # 具体工厂
    def create_payment(self):
        return Ali_Prod(huabei=1)


class Abs_Prod(metaclass=abc.ABCMeta):  # 抽象产品
    @abc.abstractmethod
    def pay(self):
        pass


class Ali_Prod(Abs_Prod):  # 具体产品
    def __init__(self, huabei=False):
        self.huabei = huabei

    def pay(self):
        if self.huabei:
            print("选择花呗支付")
        else:
            print("选择阿里支付")


class QQ_Prod(Abs_Prod):
    def pay(self):
        print("选择QQ支付")


a = HuaBei_Factory()
b = a.create_payment()
b.pay()

"""
优点:
每个具体产品都对应一个具体工厂类，不需要修改工厂类代码.更贴合单一接口原则，
有更多功能单一的工厂．
隐藏了对象创建的实现细节，就像Ali_Prod（）传入(huabei=1)就能调用花呗支付，
可是我依旧新建了工厂，这样用户就不知道实现的细节．

缺点:
每增加一个具体产品类，就必须增加一个相应的具体工厂类"""
