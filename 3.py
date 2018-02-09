newlist = []
list1 = []
from openpyxl import load_workbook
wb = load_workbook(filename = 'city.xlsx')
sheet_ranges = wb['Sheet1']
list_or = (sheet_ranges['A1:A84'].value)
list1.append(list_or)

for word in list1:
    word = word.split(', ')
    newlist.extend(word)

in_city = input("도를 입력해주세요\n")
in_adr = input("시군구를 입력해주세요\n")


for a in newlist:
    if a == in_str:
        print("교평받아라")
        import sys
        sys.exit()
print("안해도 됨 ㅋㅋ")
