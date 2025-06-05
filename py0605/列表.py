lst=['hello','world',90]
print(lst)
for item in lst:
    print(item)
for i in range(0,len(lst)):
    print(i,'---',lst[i])
for index,item in enumerate(lst,1):
    print(index,item)
for index,item in enumerate(lst):
    print(lst[index])