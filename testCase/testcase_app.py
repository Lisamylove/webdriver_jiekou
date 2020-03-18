import unittest
import requests

url_userLogin = 'http://testkc3.chexiao.co/api/user/login'
url_list = 'http://testkc3.chexiao.co/api/gongdan/newSearchGongdanList?'
url_time = 'http://testkc3.chexiao.co/api/gongdan/updateReserveTime?'
installOrder = 'http://testkc3.chexiao.co/api/gongdan/installOrder?'
# app登录接口
params_Login = \
    {
        'uname': 'dongbeiquyuanzhuang',
        'upwd': '88b0ad730ba24bcee42ca8cf78e87934c0d6b6461418b59df58c406b6bade144'
    }
response_user = requests.post(url=url_userLogin, data=params_Login)
token = response_user.json()['data']['token']
print('登录成功:', token)

# 获取待结单列表的数据接口
params_GongDanList = \
    {
        'customerName': '',
        'endTime': '',
        'gongdanState': '12',
        'name': '',
        'page': '1',
        'pageSize': '20',
        'reserveType': '-1',
        'startTime': '',
        'token': token,
    }


class MyTest(unittest.TestCase):
    def setUp(self):
        print('case start')

    def tearDown(self):
        print('case 结束')

    def test_1_UpdateTime(self):
        # 先获取列表的数据
        response_gondanList = requests.post(url=url_list, data=params_GongDanList)
        order_list = response_gondanList.json()['data']['orderList']
        print('输入选择哪条数据:')
        index = int(input())
        params_time = \
            {
                'token': token,
                'orderid': order_list[index]['orderId'],          # 工单id
                'reserveTime': '2020-4-20 10:48:15',
            }
        # 给工单填写预约时间
        response_time = requests.post(url=url_time, data=params_time)
        print(response_time.json())

        res = requests.post(url=installOrder, data=params_time)
        print(res.json())


if __name__ == '__main__':
    unittest.main()
