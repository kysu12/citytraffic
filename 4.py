from openpyxl import load_workbook

wb = load_workbook(filename = 'city.xlsx')
sheet_ranges = wb['Sheet1']
state = 0
list1 = []
while state < 84:
    state = state + 1
    list_or = (sheet_ranges['A'+str(state)].value)
    list1.append(list_or)

a_1 = []
result =[]
for b_1 in list1:
    a_1 = b_1.split(" ")
    result.append(a_1)

re_grand1 = result[0:8]

re_grand2 =[]
for re_g in re_grand1:
    a_g = re_g[0]
    re_grand2.append(a_g)

in_city = input("도를 입력해주세요\n")
in_adr = input("시군구를 입력해주세요\n")

for re_gg in re_grand2:
    if in_city == re_gg:
        print ("특별,광역시, 도시교통정비지역입니다.")
        import sys
        sys.exit()

re_small1 = result[8:84]

e_city = []
for re_s in re_small1:
    if re_s[0] == in_city:
        e_city.append(re_s[1])
for re_ss in e_city:
    if in_adr == re_ss:
        print("도시교통정비지역입니다.")
        import sys
        sys.exit()

print("교통권역입니다.")
