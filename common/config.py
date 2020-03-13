# 登录
url_login = 'http://testfkapi3.chexiao.co/login'
# 装机接口
url_toAdd = 'http://testfkapi3.chexiao.co/phx/gongdan/customer/toAdd'
# 装机提交
url_add = 'http://testfkapi3.chexiao.co/phx/gongdan/customer/add'
played = \
    {
        'username': 'xinxinceshi',
        'password': '961111',
        'code': '1'
    }
headers = \
    {
        'Host': 'testfkapi3.chexiao.co',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
        'Referer': 'http://testfk3.chexiao.co/',
        'Cookie': 'JSESSIONID=419B31D1AC8F6A43A25654C4596A6932'
    }
# 装机工单接口参数
params = \
    {
        'orderNum': '',     # 订单编号
        'name':	'通过接口下工单',   # 车主姓名
        'frame_no':	'ZAXSSSSSDC4455595',    # 车架号
        'carBelongId':	'972532754605248',  # 部门/组织id
        'brand': '车牌号',    # 车辆品牌
        'model': '型号',  # 车辆型号
        'plate_no': '晋ML958',     # 车牌号
        'tel': '13254545454',   # 车主电话
        'driverIdNum': '140825190011110098',    # 身份证号
        'family_province': '35',      # 家庭省
        'family_city': '60',          # 家庭市
        'family_address': '4343',       # 家庭详细地址
        'working_province': '',     # 工作省
        'working_city': '',         # 工作市
        'working_address': '',      # 工作详细地址
        'wire_equip': '1',          # 有线设备
        'wireless_equip': '0',      # 无线设备
        'obd_equip': 0,             # obd设备
        'contact_status': '43',     # 联系人身份
        'contact_name':	'43',       # 联系人姓名
        'contact_tel':	'4343434',  # 联系人电话
        'planInstallTime':	'2020-03-13 15:51:30',  # 计划安装时间
        'install_province':	'580',  # 安装省
        'install_city':	'629',  # 安装市
        'install_location':	'434343',   # 安装详细地址
        'installWay': '0',      # 安装方式 0车晓安装  1客户自行安装
        'installBelong': '0',   # 安装归属0和3为车晓安装  2 客户自行安装（先锋专属）
        'customerId': '0',      # 所属客户id
        'carryInsurance': '0',
        'credit_period': '0',   # 贷款年限
        'dealer': '',       # 经销商
        'install_remark': '',       # 工单备注
        'carColor': '',     # 车辆颜色
        'systemNum': '',        # 项目编号
        'businessType': '',     # 业务类型 0新车  1二手车
        'carPrice': '',         # 车辆价格范围
        'contract': '',
        'contractPhone': '',
        'purchasePrice': '',
        'insurancePrice': '',
        'projectGroup': '',     # 项目分组（1常规 2万元购项目 3悟空项目 4直租车项目）
    }
