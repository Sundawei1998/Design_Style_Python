"""
内容:将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

角色:
抽象建造者
具体建造者
指挥者
产品

使用场景：
建造者模式与抽象工厂模式相似，也用来创建复杂对象。主要区别是建造者模式着重一步步按顺序构造一个复杂对象，
而抽象工厂模式着重于一个工厂能生成多个互相限制搭配的产品。

"""
import abc


class Player():
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s, %s，%s" % (self.face, self.body, self.arm, self.leg)


# 抽象建造者
class PlayerBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def build_face(self):
        pass

    @abc.abstractmethod
    def build_body(self):
        pass

    @abc.abstractmethod
    def build_arm(self):
        pass

    @abc.abstractmethod
    def build_leg(self):
        pass


# 具体建造者
class SexyGirlBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条身材"

    def build_arm(self):
        self.player.arm = "漂亮胳膊"

    def build_leg(self):
        self.player.leg = "大长腿"


# 具体建造者
class MonsterBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸蛋"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "怪兽胳膊"

    def build_leg(self):
        self.player.leg = "怪兽腿"


# 指挥者
class PlayerDirector():  # 控制组装顺序
    def buildplayer(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


builder = SexyGirlBuilder()
director = PlayerDirector()
print(director.buildplayer(builder))


"""
优点:
隐藏了一个产品的内部结构和装配过程
将构造代码与表示代码分开
可以对构造过程进行更精细的控制
"""
