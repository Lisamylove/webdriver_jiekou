import requests
from common.config import *
import unittest
import warnings


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('case start')

    def tearDown(self):
        print('case end')
        print('--------------------------------------------------')

    def test_1_login(self):
        # 登录
        url_login = 'http://testfkapi3.chexiao.co/login'
        response = requests.post(url=url_login, data=played, headers=headers)
        s = response.cookies
        print(s)
        print("登录成功:", response.status_code)
        return s

    def test_2_toAdd(self):
        # 装机接口
        url_toAdd = 'http://testfkapi3.chexiao.co/phx/gongdan/customer/toAdd'
        session = requests.Session()
        response2 = session.post(url=url_toAdd, data=played, headers=headers, cookies=self.test_1_login())
        toadd_data = response2.json()
        print(toadd_data)
        print("点击装机按钮", response2.status_code)

    def test_3_add(self):
        # 装机提交
        url_add = 'http://testfkapi3.chexiao.co/phx/gongdan/customer/add'
        session = requests.Session()
        response_add = session.post(url=url_add, data=played, headers=headers, params=params_add, cookies=self.test_1_login())
        add_data = response_add.json()
        print(add_data)
        print("填写工单信息，提交工单:", response_add.status_code)

    def test_4_list(self):
        url_list = 'http://testfkapi3.chexiao.co/phx/gongdan/customer/list'
        response_list = requests.post(url=url_list, data=played, headers=headers, cookies=self.test_1_login(), params=params_list)
        print('获取列表数据成功')
        return response_list.json()

    def test_5_check(self):
        # 审核工单接口
        url_check = 'http://testfkapi3.chexiao.co/phx/gongdan/admin/check'
        # 提交审核接口的参数
        params_check = \
            {
                'parentOrgId': '',
                'frame_no': self.test_4_list()['data']['dataList'][0]['frame_no'],
                'id': self.test_4_list()['data']['dataList'][0]['id'],
                'remarknew': '',
                'gongdanState': self.test_4_list()['data']['dataList'][0]['gongdanState'],
                'install_id': '0',
                'install_remark': '',
                'gongdanType': '0'
            }
        # 将工单置为待调度状态
        params_check.update({'gongdanState': '11'})
        response_check = requests.post(url=url_check, data=played, headers=headers, cookies=self.test_1_login(), params=params_check)
        print('工单置为待调度状态', response_check.json())
        # 将工单调度到东北区域安装公司
        params_check.update({'gongdanState': '12', 'install_id': '990552595259968'})
        response_check = requests.post(url=url_check, data=played, headers=headers, cookies=self.test_1_login(), params=params_check)
        print('将工单调度到东北区域安装公司', response_check.json())


if __name__ == '__main__':
    unittest.main()

