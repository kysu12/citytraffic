newlist = []
list1= ["aaa, ddd,dddB"]
for word in list1:
    word = word.split(',')
    newlist.extend(word)

print(newlist)
print(type(newlist))
