"""
内容:
为其他对象提供—种代理以控制对这个对象的访问。


应用场景:
远程代理:为远程的对象提供代理.类似django操作mysql,其实底层都是＂建立连接－拿到游标－
执行mysql语句＂，但是orm只用了一个关键字就把这个过程浓缩了，此时orm关键字就是那个mysql
过程的代理.
虚代理:根据需要创建很大的对象.当原本接口创建对象是把一个大文件加载在内存存起来
的时候，可以用虚代理把原本的创建过程包起来，不要还没调用就加载到内存
保护代理:控制对原始对象的访问，用于对象有不同访问权限时，类似vpn.

角色:
抽象实体(Subject)
实体(RealSubject)
代理(Proxy)

"""

from abc import ABCMeta, abstractmethod


# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, "r", encoding="utf-8")  # 我们自己不要这样写，一创建实例就把大文件读到内存
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, "w", encoding="utf-8")
        f.write(content)
        f.close()


# 代理(虚代理，让他不要加载那么大文件，可以用在无图模式上)
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


# 代理(保护代理，在实体的某些接口上二次开发，可以用在权限划分上)
class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content=None):
        print("我要在这里加一些操作")
        raise PermissionError("无写入权限")


print(VirtualProxy("代理模式创建的超级无敌大文件.txt").set_content("哎呀，你干嘛～～"))
print(VirtualProxy("代理模式创建的超级无敌大文件.txt").get_content())

print(ProtectedProxy("代理模式创建的超级无敌大文件.txt").set_content())
print(ProtectedProxy("代理模式创建的超级无敌大文件.txt").get_content())

"""
优点:
远程代理:可以隐藏对象位于远程地址空间的事实
虚代理:可以进行优化，例如根据要求创建对象
保护代理:允许在访问一个对象时有一些附加的内务处理
"""
