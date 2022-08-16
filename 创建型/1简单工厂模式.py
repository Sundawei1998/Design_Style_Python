"""
内容:不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。

角色︰
工厂角色(Creator)
抽象产品角色(Product)
具体产品角色(Concrete Product)

使用场景:
当你创建某个类需要往里面传入很多参数，但是你又不想让客户这么麻烦去输入那些参数，
你就可以用简单工厂模式，帮他完善这些需要输入的信息，帮他创建这个类．
"""
import abc


class Payment(metaclass=abc.ABCMeta):  # 改变元类，继承新的元类，新的元类里面才有这个装饰器
    @abc.abstractmethod  # 实例化的时候这个方法无法被实例化，因此继承了这个类的方法被实例化的时候就
    # 需要重写pay方法，代表这是个抽象化类，只能继承无法实例化．
    def pay(self, money):
        print(money)
        pass

class Ali_System(Payment):
    def pay(self):
        print("选择阿里支付")


class QQ_System(Payment):
    def pay(self):
        print("选择QQ支付")


class PaymentFactory:
    def create_payment(self, method, ):
        if method == "alipay":
            return Ali_System()
        elif method == "qqpay":
            return QQ_System()
        else:
            raise TypeError("输入错误，没有这种输入方式")


a = PaymentFactory()
b = a.create_payment("alipay")
b.pay()

"""
优点:
隐藏了对象创建的实现细节客户端不需要修改代码
缺点︰
违反了单一职责原则,将创建逻辑几种到一个工厂类里当添加新产品时，需要修改工厂类代码，违反了开闭原则
"""
