"""
内容:
将一个事物的两个维度分离，使其都可以独立地变化。

适用场景:
当事物有两个维度上的表现，两个维度都可能扩展时。

角色:
抽象(Abstraction)
细化抽象(RefnedAbstraction)
实现者(lmplementor)
具体实现者(Concretelmplementor)


"""
import abc


class Shape(metaclass=abc.ABCMeta):#实现者
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def draw(self):
        pass


class Color(metaclass=abc.ABCMeta):#抽象
    @abc.abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):#具体实现
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):#具体实现
    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Red(Color):#细化抽象
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Green(Color):#细化抽象
    def paint(self, shape):
        print("绿色的%s" % shape.name)

a = Red()
b = Rectangle(a)
b.draw()

"""
优点︰
抽象和实现相分离
优秀的扩展能力"""