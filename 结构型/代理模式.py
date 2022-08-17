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

"""

from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, "a",encoding="utf-8")
        self.content = f.read()
        f.close()
    def get_content(self):
        return self.content
    def set_content(self,content):
        f =open(self.filename, "w",encoding="utf-8")
        f.write(content)
        f.close()
RealSubject("aa.txt")