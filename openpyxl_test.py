'''
Test file for openpyxl functionality to preserve / edit excel formatting
'''


import openpyxl as pxl
import re


wb = pxl.load_workbook(filename="EE_RAW.xlsx")

print(wb.sheetnames)

sheet = wb.active

# sheet["A1"] = "gang gang"
# sheet["A10"] = "something else"


for cell in sheet["A"]:
    print(cell.value)


