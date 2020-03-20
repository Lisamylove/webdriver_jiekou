from common.configURL import *
import requests
from common.config import *
import unittest
import warnings


def login_cookie():
    # 首先需要登录
    response = requests.post(url=url_login, data=played, headers=headers)
    cookie = response.cookies
    print(cookie)
    return cookie


def page_list():
    # 获取列表的数据，返回的数据信息用于后面的数据处理
    response_list = requests.post(url=url_web_list, data=played, headers=headers, cookies=login_cookie(), params=params_list)
    print('获取列表数据成功')
    print(response_list.json())
    dataList = response_list.json()['data']['dataList']
    return dataList


# 提交审核接口的参数
params_check = \
    {
        'parentOrgId': '',
        'frame_no': page_list()[0]['frame_no'],
        'id': page_list()[0]['id'],
        'remarknew': '',
        'gongdanState': page_list()[0]['gongdanState'],
        'install_id': '0',
        'install_remark': '',
        'gongdanType': '0'
    }


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('case start')

    def tearDown(self):
        print('case end')

    def test_1_toAdd(self):
        # 装机
        session = requests.Session()
        response2 = session.post(url=url_toAdd, data=played, headers=headers, cookies=login_cookie())
        print("点击装机按钮:", '\n', response2.json())

    def test_2_add(self):
        # 装机提交
        session = requests.Session()
        response_add = session.post(url=url_add, data=played, headers=headers, params=params_add, cookies=login_cookie())
        print("填写工单信息，提交工单:", '\n', response_add.json())

    def test_3_check(self):
        # 将工单置为待调度状态
        params_check.update({'gongdanState': '11'})
        response_check = requests.post(url=url_check, data=played, headers=headers, cookies=login_cookie(), params=params_check)
        print('工单置为待调度状态:', '\n', response_check.json())

        # 将工单调度到东北区域安装公司
        params_check.update({'gongdanState': '12', 'install_id': '990552595259968'})
        response_check = requests.post(url=url_check, data=played, headers=headers, cookies=login_cookie(), params=params_check)
        print('将工单调度到东北区域安装公司:', '\n', response_check.json())


if __name__ == '__main__':
    unittest.main()

