lst=[
    ['a','f','c'],
    ['f','d','s'],
    ['a','e','e']
]
for row in lst:
    for item in row:
        print(item,end='\t')
    print()
lst2=[ [j for j in range(5)] for i in  range(5)]
for row in lst2:
    for item in row:
        print(item,end='\t')
    print()