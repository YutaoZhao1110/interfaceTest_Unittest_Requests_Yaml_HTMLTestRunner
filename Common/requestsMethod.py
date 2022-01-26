#coding = "utf-8"

import requests
import json
import urllib3


urllib3.disable_warnings()#去掉一些warnings

class RequestsMethodSelect:
    def post_Method(self, url, header, data):
        res = requests.post(url = url,headers = header,data= json.dumps(data),verify = False)
        #json.dumps(data)把文件转成json格式方便使用;verify = False 避免ssl认证
        return res
    def get_Method(self, url, header, data = None):
        res = requests.get(url = url,headers = header, data = json.dumps((data)),verify = False)
        return  res

    def run_main(self, method, url, header, data = None):
        res = None
        if method == "post":
            res = self.post_Method(url, header, data )
        if method == "get":
            res = self.get_Method(url, header, data = None)
        return res

url = "http://www.baidu.com"
heder = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
}

