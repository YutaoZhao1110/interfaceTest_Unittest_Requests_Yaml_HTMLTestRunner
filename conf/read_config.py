#coding:utf-8
import configparser
import os
"""
读取配置文件中的信息,并且以字典的形式
"""
class ReadConfig:
    def __init__(self):
        #1获取文件路径2添加文件名添加
        dir_path = os.path.dirname(os.path.realpath(__file__))
        conf_path = os.path.join(dir_path, "config.ini")
        #创建ConfigParser对象
        self.conf = configparser.ConfigParser()
        #read(filename)—直接读取文件内容
        self.conf.read(conf_path, encoding= "utf-8")

    def readconfig(self,param):
        #获取section（param）下面的所有键值对，以字典形式返回
        item = dict(self.conf.items(param))
        return item
if __name__ == '__main__':
    rf = ReadConfig()
    rf.readconfig("mail")
