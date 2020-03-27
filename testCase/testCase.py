'''
功能描述：
根据测试数据，获取测试数据，完成接口测试的请求，断言结果

解析：
    1-调用readExcel模块，获取测试数据
    2-根据接口测试数据，进行请求
        2.1-get请求-get方法
        2.2-post请求post方法
        。。。
    3-断言每个接口返回的结果
        3.1-成功
        3.2-失败
    4-结果写入到excel
'''
from common.readExcel import readExcel
import requests
import json
import unittest
from ddt import ddt,data,unpack
from common.configHttp import ConfigHttp
from common.readConfig import ReadConfig
# from common.writeExcel import WriteExcel
from common.writeExcel import WriteExcel

#python编写测试用例必须继承unittest.TestCase
re = readExcel()
test_data = re.read()
rc = ReadConfig()
cf = ConfigHttp()
wr = WriteExcel()

@ddt
class testCase(unittest.TestCase):
# 1 - 调用readExcel模块，获取测试数据
#
#     def setUp(self) -> None:
#         re = readExcel()
#         self.test_data = re.read()

    @data(*test_data)
    @unpack
    def testRun(self,id,urlstr,name,method,param,expect,real,status):
        header = {'User-Agent': 'Mozilla/6.0'}
        print("url:",urlstr)
        print('param:',param)
        print('expect:', expect)

        re = cf.getRequest(urlstr,method, param)
        real = re.json()['errorCode']
        print('id:', id, "real:", real, "expect:", expect)
        try:
            status = self.assertEqual(real, eval(expect))
            print("status:=================", status)

        except BaseException as m :
            print(urlstr)
            print(param)
            # print('id:', id, "real:",real,"expect:", expect)
            print(re.text)
            status = 'Error'
        finally:
            pass
            if status == None:
                wr.writeData(int(id), int(real), 'sucess')
            else:
                wr.writeData(int(id), int(real), 'fail')








    # 2 - 根据接口测试数据，进行请求
    # 2.1 - get请求 - get方法
    # 2.2 - post请求post方法
    # 。。。
    # 3 - 断言每个接口返回的结果

    # 3.1 - 成功
    # 3.2 - 失败
    # 4 - 结果写入到excel


if __name__ == '__main__':
    unittest.main()

