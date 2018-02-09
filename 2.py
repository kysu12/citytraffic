list1 = []
from openpyxl import load_workbook
wb = load_workbook(filename = 'city.xlsx')
sheet_ranges = wb['Sheet1']
state = 0
while state < 84:
    state = state + 1
    list_or = (sheet_ranges['A'+str(state)].value)
    list1.append(list_or)

a_1 = []
result =[]
for b_1 in list1:
    a_1 = b_1.split(" ")
    result.append(a_1)


in_city = input("도를 입력해주세요\n")
in_adr = input("시군구를 입력해주세요\n")

for a in result:
    if a == in_str:
        print("교평받아라")
        import sys
        sys.exit()
print("안해도 됨 ㅋㅋ")
