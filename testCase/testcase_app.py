import unittest
import requests
import json
from common.configURL import *
from common.configPart import *
from common.configIMG import *


def login_token():
    # 首先需要进行登录，获取token
    res_user = requests.post(url=url_userLogin, data=data_Login)
    token = res_user.json()['data']['token']
    print('登录成功token:', token)
    return token


def order_list():
    # 获取列表的数据
    res_information = requests.post(url=url_list, data=data_information, headers=headers)
    orderList = res_information.json()['data']['orderList']
    return orderList


def order_id():
    print('要接单的VIN是哪个:')
    frame_no = input()
    for index in range(len(order_list())):
        if order_list()[index]['frameNo'] == frame_no:
            print(order_list()[index]['orderId'])
        return order_list()[index]


headers = {'token': login_token()}
data_orderId = {'orderid': order_id()['orderId']}


class MyTest(unittest.TestCase):
    def setUp(self):
        print('case start Welcome')

    def tearDown(self):
        print('case end bai')

    def test_1_ReserveTime(self):
        # 给工单填写预约时间
        data_orderId.update({'reserveTime': '2020-5-20 10:48:15'})
        res_time = requests.post(url=url_time, data=data_orderId, headers=headers)
        print('工单填写预约时间', res_time.json())
        res_time = requests.post(url=url_installOrder, data=data_orderId, headers=headers)
        print('工单改变状态', res_time.json())

    def test_2_install(self):
        # 更新获取数据接口的参数信息
        data_information.update({'gongdanState': '21', 'reserveType': '1'})
        order_list()
        # 获取安装的工单的信息
        data_orderId.update({'gongdan_state': order_id()['orderStatus']})
        res_getId = requests.post(url=url_getId, data=data_orderId, headers=headers)
        print('获取工单信息', '\n', res_getId.json())
        # 安装设备
        res_deviceNum = requests.post(url=url_deviceNum, data=data_deviceNum, headers=headers)
        print('安装设备:', res_deviceNum.json())
        # 测试设备
        data_test_device.update({'orderid': order_id()['orderId']})
        res_test_device = requests.post(url_test_device, data=data_test_device, headers=headers)
        print(res_test_device.json())


        # 工单上传图片信息
        install_img = res_getId.json()['data']['installImg']
        print(install_img)
        img_list = install_img.split(',')
        print(img_list)     # 用逗号隔开，转换成集合
        global img
        pictureIds = []
        img = 0
        for img in range(len(img_list)):
            if img == 0:
                res_img = requests.post(url=url_img, files=file_f1, data=data_orderId, headers=headers)
            elif img == 1:
                res_img = requests.post(url=url_img, files=file_f2, data=data_orderId, headers=headers)
            elif img == 2:
                res_img = requests.post(url=url_img, files=file_f3, data=data_orderId, headers=headers)
            elif img == 3:
                res_img = requests.post(url=url_img, files=file_f4, data=data_orderId, headers=headers)
            elif img == 4:
                res_img = requests.post(url=url_img, files=file_f5, data=data_orderId, headers=headers)
            elif img == 5:
                res_img = requests.post(url=url_img, files=file_f6, data=data_orderId, headers=headers)
            elif img == 6:
                res_img = requests.post(url=url_img, files=file_f7, data=data_orderId, headers=headers)
            elif img == 7:
                res_img = requests.post(url=url_img, files=file_f8, data=data_orderId, headers=headers)
            elif img == 8:
                res_img = requests.post(url=url_img, files=file_f9, data=data_orderId, headers=headers)
            print('照片信息', '\n', res_img.json())
            pictureIds.append(res_img.json()['data']['fileId'])
            img += 1
        print(pictureIds)

        # 提交安装信息
        data_finish.update({'orderid': order_id()['orderId'], "pictureIds": ','.join(pictureIds)})
        res_finish = requests.post(url=url_finish, data=data_finish, headers=headers)
        print(','.join(pictureIds))
        # print(res_finish.json())


if __name__ == '__main__':
    unittest.main()
