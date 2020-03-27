'''
功能描述：在Excel中取出测试数据，最终以列表的形式存储
解析：
   1-找到目标Excel文件,并打开
   2-定位sheet页
   3-定位目标行
   4-读取
   5-按照预期的数据格式进行组装数据
'''

import xlrd
import os


p = os.path.abspath(__file__)
dirname = os.path.dirname(p)
dirname = os.path.dirname(dirname)
p = dirname + r'\testData\data.xls'

class readExcel(object):
    #定义属性
    def __init__(self):
        self.readbook = xlrd.open_workbook(p)

    def read(self):
        sheet =self.readbook.sheet_by_index(0)
        nrows = sheet.nrows
        data = []
        for n in range(1, nrows):
            row_value = sheet.row_values(n)
            # print(row_value)
            # print("========")
            print(row_value)
            data.append(row_value)
        return data


if __name__ == '__main__':
    r = readExcel()
    r.read()



