list1 =[]
from openpyxl import load_workbook
wb = load_workbook(filename = 'city.xlsx')
sheet_ranges = wb['Sheet1']
list_or = (sheet_ranges['A2'].value)
list1.append(list_or)
print(list1)
