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

re_grand1 = result[0:8]
re_grand2 =[]
for re_g in re_grand1:
    a_g = re_g[0]
    re_grand2.append(a_g)

print(re_grand2)


re_small1 = result[9:84]


re_chungbuk = []
for re_s in re_small1:
    if re_s[0] == "충청북도":
        re_chungbuk.append(re_s[1])
print(re_chungbuk)

re_chungnam = []
for re_s in re_small1:
    if re_s[0] == "충청남도":
        re_chungnam.append(re_s[1])

re_jeonbuk = []
for re_s in re_small1:
    if re_s[0] == "전라북도":
        re_jeonbuk.append(re_s[1])

re_jeonnam = []
for re_s in re_small1:
    if re_s[0] == "전라남도":
        re_jeonnam.append(re_s[1])

re_kyengbuk = []
for re_s in re_small1:
    if re_s[0] == "경상북도":
        re_kyengbuk.append(re_s[1])

re_kyengnam = []
for re_s in re_small1:
    if re_s[0] == "경상남도":
        re_kyengnam.append(re_s[1])

re_jeju = []
for re_s in re_small1:
    if re_s[0] == "제주특별자치도":
        re_jeju.append(re_s[1])
