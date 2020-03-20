# app登录接口参数
data_Login = \
    {
        'uname': 'dongbeiquyuanzhuang',
        'upwd': '88b0ad730ba24bcee42ca8cf78e87934c0d6b6461418b59df58c406b6bade144'
    }

# 获取待结单列表的数据接口
data_information = \
    {
        'customerName': '',
        'endTime': '',
        'gongdanState': '12',
        'name': '',
        'page': '1',
        'pageSize': '20',
        'reserveType': '-1',
        'startTime': '',
    }
print('请输入安装设备:')
deviceNum = input()
data_deviceNum = \
    {
        'deviceNum': deviceNum
    }
# 测试设备
data_test_device = \
    {
        'repairType': '1',
        'checkInstall': '1',
        'devicenum': data_deviceNum['deviceNum'],
    }

data_finish = \
    {
        "installEnvironment": "",
        "installname": "2121",
        "installtel": "13254545454",
        "wire_equiplist": [
            {
                "devicenum": data_deviceNum['deviceNum'],
                "devicelocation": "左A柱"
             }
        ],
        "wireless_equiplist": [
            ],
        "obd_equiplist": []
    }
