#codind:utf-8

import unittest
import os
import sys  # 导入sys模块
from common.HTMLTestRunnerPlugins import HTMLTestRunner


sys.setrecursionlimit(30000)  # 将默认的递归深度修改为3000

"""
https://blog.csdn.net/ly021499/article/details/89383439
"""

class Read_config_Caselist:
    def read_config_CaseListMetod(self, config_FileName):
        """
        :param config_FileName:
        :return: 以字典的形式返回用例列表
        :note:使用读取txt文件的形式生成testPlan
        """
        #创建空列表，定义为全局变量，后边的方法也可以惊醒调用
        global caseList
        caseList = []

        dir_path = os.path.dirname(os.path.realpath(__file__))
        conf_path = os.path.join(dir_path,config_FileName)
        with open(conf_path )as f:
            #按照行进行读取追加列表中，空和#不读取
            fp = f.read()
            cases = fp.splitlines()#方法将字符串拆分为列表
            for case in cases:
                # 以井号开头不读取
                if case and not case.startswith("#"):
                    caseList.append(case)

            return caseList

    def get_runCase(self):
        """
        :note:create null testsuit ，add testcase into testsuit for run
        :return:
        """
        suit_module = []
        print(caseList)


        # 如果用例名称在txt中是执行状态，则把在testCase文件夹下相同用例名称的py文件追加到一个列表suit_modle中
        for case in caseList:

            discover = unittest.defaultTestLoader.discover("../testCase/", pattern= case + ".py" ,top_level_dir=None)

            #suit_module.append(discover)
        # suit_module.append("test_login.py")

        # if len(suit_module) >0:
        #     for test_suit in suit_module:
        #         suit = unittest.TestSuite()
        #         """addTest()：添加单个用例
        #         addTests()：添加多个用例"""
        #         suit.addTest(test_suit)




if __name__ == '__main__':
    readCaseList = Read_config_Caselist()
    readCaseList.read_config_CaseListMetod("config_runCaseList.txt")
    readCaseList.get_runCase()

