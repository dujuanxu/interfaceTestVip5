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
# from common.readExcel import readExcel
import requests
import unittest
from ddt import ddt,data,unpack

#python编写测试用例必须继承unittest.TestCase

@ddt
class MyTestCase(unittest.TestCase):

    # @data(1)
    # def test_normal(self, value):
    #     print(value)
    #     self.assertEqual(value,1)
    #
    # @data(2,3,4)
    # def test_normal2(self, value):
    #     print(value)
    #     self.assertEqual(value,2)

    @data([1,2],[2,3])
    @unpack
    def test_normal3(self,value1, value2):
        print(value1,value2)
        self.assertEqual(1,1)

    # @data({'value1':1,'value2':2},{'value1':3, 'value2':4})
    # @unpack
    # def test_dict(self,value1, value2):
    #     print(value1,value2)


if __name__ == '__main__':
    unittest.main()
