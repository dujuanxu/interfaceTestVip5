import os
import xlrd
from xlutils.copy import copy

class WriteExcel(object):
    def __init__(self):
        p = os.path.abspath(__file__)
        dirname = os.path.dirname(p)
        dirname = os.path.dirname(dirname)
        self.p = dirname + r'\testData\data.xls'
        readbook = xlrd.open_workbook(self.p)
        self.readbook_cp = copy(readbook)
        self.sheet_cp = self.readbook_cp.get_sheet(0)

    def writeData(self, id, real, status):

        print("")
        print('%%%%%%%%%%%%%wirte:%%%%', id, real, status)
        print('%%%%%%%%%%%%wirte path', self.p)
        try:
            self.sheet_cp.write(id, 6, real)
            self.sheet_cp.write(id, 7, status)
            # os.remove(self.p)
            self.readbook_cp.save(self.p)
        except BaseException as m:
            print(m)


if __name__ == '__main__':
    w = WriteExcel()
    w.writeData(1, 0, 'sucsess  00')
    w.writeData(2,-1,'fail')
    w.writeData(3,0,'sucsess 22')





