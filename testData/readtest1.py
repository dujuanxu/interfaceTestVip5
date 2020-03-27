import xlrd
# import xlwt

readbook = xlrd.open_workbook(r'data.xls')
sheet = readbook.sheet_by_index(0)
rowdata = sheet.row_values(0)

nrows = sheet.nrows
print(nrows)