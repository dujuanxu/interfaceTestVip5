import os
import xlrd
from xlutils.copy import copy

from common.writeExcel import WriteExcel

wr = WriteExcel()
wr.writeData(1, 0, '888888hhh334455fffffafsda444555999')
wr.writeData(2, -1, '99999hhh4455ffffrrrrffff444555777')
wr.writeData(3, 0, '00000000hhhffffdddffffrrrr44445666777999')

#
