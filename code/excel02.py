# coding=gbk
# excel排序,打开指定文件并对"item[1]第二列"进行排序,并保存在指定文件中.
# 需求:
# 商品名称    商品价格    商品数量

# - 定义一个函数， readwb(wbname, sheetname=None)
# - 如果用户指定sheetname就打开用户指定的工作表， 如果没有指定， 打开active sheet;
# -  根据商品的价格进行排序(由小到大)， 保存到文件中;商品名称:商品价格:商品数量

import openpyxl


def readwb(wbname, sheetname=None):
    workbo = openpyxl.load_workbook(wbname)
    if not sheetname:
        sheet = workbo.active
    else:
        sheet = sheetname
    wb_info = []
    for row in sheet.rows:
        row_info = [val.value for val in row]
        wb_info.append(row_info)
    return sorted(wb_info, key=lambda item:item[2])


def save_to_excel(data, wbname, wbsheet='Sheet1'):
    workbo = openpyxl.Workbook()
    sheet = workbo.active
    for row_index,row in enumerate(data):
        for column_index,cell_value in enumerate(row):
            sheet.cell(row=row_index+1, column=column_index+1, value=cell_value)
    workbo.save(wbname)


excel_info = readwb('example.xlsx')
save_to_excel(excel_info, 'modify.xlsx')


