import os
import xlrd
from xlutils.copy import copy

# from common.writeExcel import WriteExcel
#
# wr = WriteExcel()
# wr.writeData(1, 0, '888888hhh334455fffffafsda444555999')
# wr.writeData(2, -1, '99999hhh4455ffffrrrrffff444555777')
# wr.writeData(3, 0, '00000000hhhffffdddffffrrrr44445666777999')

#比较2个版本version1"1.12.1"和"1.12.3"哪个版本号大



def get_max_version(version1, version2):
    l1 = version1.split('.')
    l2 = version2.split('.')

    i = 0
    while i < len(l1) and i <len(l2):
        if int(l1[i]) > int(l2[i]):
            return version1
        elif int(l1[i]) < int(l2[i]):
            return version2
        i += 1
    return version1

print(get_max_version('1.3.3', '1.12.2'))








