import requests
from common.config import *
import unittest
import warnings


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        pass

    def tearDown(self):
        pass

    def test_case_login(self):
        response = requests.post(url=url_login, data=played, headers=headers)
        login_data = response.json()
        # 断言
        self.assertEqual('xinxinceshi', login_data['data']['user']['userName'])
        self.assertEqual('席鑫鑫测试账号', login_data['data']['user']['nickName'])
        self.assertIn('419B31D1AC8F6A43A25654C4596A6932', login_data['data']['sessionId'])
        print("login_code登录:", response.status_code)

    def test_case_add(self):
        session = requests.Session()
        response_add = session.post(url=url_add, data=played, headers=headers, params=params)
        add_data = response_add.json()
        self.assertEqual(1, add_data['data']['code'])
        print(add_data)
        print("add_code工单提交:", response_add.status_code)

    def test_case_toAdd(self):
        session = requests.Session()
        response2 = session.post(url=url_toAdd, data=played, headers=headers)
        toadd_data = response2.json()
        self.assertNotEqual(7, toadd_data['data']['code'])
        print("toAdd装机接口状态", response2.status_code)


if __name__ == '__main__':
    unittest.main()

