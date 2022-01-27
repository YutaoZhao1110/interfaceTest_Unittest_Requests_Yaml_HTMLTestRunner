import unittest
import time
from common.getReportinfo import tast_demo1
from common.HTMLTestRunnerPlugins import HTMLTestRunner



#获取目录地址
test_dir = "./testCase"
disc = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")


if __name__ == '__main__':
    reportInfo = tast_demo1().get_reportInfo()
    with open(reportInfo, "wb") as f:

        runner = HTMLTestRunner(
                                title= time.strftime("%Y-%m-%d %H-%M") + "自动化测试报告",
                                description="简介",
                                stream=f,
                                verbosity=2)
        runner.run(disc)