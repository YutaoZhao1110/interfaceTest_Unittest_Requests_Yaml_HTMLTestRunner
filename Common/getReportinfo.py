import unittest
import time

class tast_demo1(unittest.TestCase):
    def get_reportInfo(self):
        report_dir = "./reports"
        date = time.strftime("%Y-%m-%d %H-%M")
        testTime = time.strftime("%H-%M")
        report_name = report_dir + "/" + date + "result.html"  # 报告文件
        return report_name
