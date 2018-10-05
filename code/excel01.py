# coding=gbk
import openpyxl
# 1.加载excel文档
workbo = openpyxl.load_workbook("example.xlsx") # <class 'openpyxl.workbook.workbook.Workbook'>
all_sheet = workbo.sheetnames   # 显示所有的工作表，['Sheet1', 'Sheet2', 'Sheet3', 'Sheet4']
active_sheet = workbo.active    # 显示活动表，<Worksheet "Sheet4">
# 2.选择要操作的工作表
print(all_sheet)
print(active_sheet)
sheet = active_sheet  # workbo['Sheet1']        # 选择要操作的工作表
title_sheet = sheet.title       # 获取工作表名称，Sheet1
print(title_sheet)
#3.查看指定的单元格信息
cell_b1 = sheet.cell(row=1,column=2)    # 查找指定单元格信息,返回一个对象，<Cell 'Sheet1'.B1>
value_b1 = cell_b1.value                # 查看指定单元格内容，17

#4.获取工作表的行数和列数
max_row = sheet.max_row         # 获取工作表行数
max_column = sheet.max_column   # 获取工作表列数
print(max_row,max_column)
#5.修改工作表信息和单元格信息
sheet.title = 'family_info'     # 修改工作表的标题
sheet['B1'] = 100               # 修改单元格值
value=sheet.cell(1,3).value     # 获取到第一行第三列的值
sheet.cell(5,3).value='abc'     # 将第五行第三列的值改为abc
print(value,sheet)
#6.访问所有单元格信息
info_row = sheet.rows               # 返回的是一个生成器，<generator object Worksheet._cells_by_row at 0x000001DB770DFF68>
for row in info_row:          # 遍历工作表，拿出每一个值
    for column in row:
        print(column.value,end=' ')
    print()

#7.保存修改信息
workbo.save('example.xlsx')
# http://www.goobiao.com/
# https://segmentfault.com/a/1190000016367370