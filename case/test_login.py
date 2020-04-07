import requests
import unittest
import ddt
import os
from setting import *
from lib.util import *

@ddt.ddt
class LoginCase(unittest.TestCase):
    #用ddt方法加载yaml文件里面的数据
    @ddt.file_data(os.path.join(DATA_PATH, 'login.yaml'))
    def test_login(self, **case):
        url = case.get("url")
        method = case.get("method")
        data = case.get("data")
        status_code = case.get('status_code')
        check = case.get("check")
        self._testMethodDoc = case.get("doc", "该用例无描述")  #加入用例描述
        #判断是否加密
        pwd = data['password']
        name = data['username']
        print(len(pwd))
        if len(pwd) == 31:
            data['password'] = pwd
        elif len(pwd) == 33:
            data['password'] = pwd
        elif name == "伊利2号":
            data["password"] = pwd
        else:
            data['password'] = hash_code(pwd)
        #根据数据构建选择请求方式
        if method.lower() == 'post':
            res = requests.post(url, data=data)
        else:
            res = requests.get(url, params=data)
        #处理结果数据，方便比较
        results = set_res_data(res.text)
        #断言，根据返回的数据判断是否包含或相等
        self.assertEqual(status_code, res.status_code)
        for c in check:
            self.assertIn(c, results)

if __name__ == '__main__':
    unittest.main()