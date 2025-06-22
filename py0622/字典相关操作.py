d={1000:'Lisa',1001:'Jack',1002:'Mark',1003:'John'}
print(d)

d[1004]='Tom'
print(d)

dkey=d.keys()
print(dkey)
print(list(dkey))
print(tuple(dkey))

ditem=d.items()
print(ditem)
print(list(ditem))
print(tuple(ditem))

print(d.pop(1002))
print(d)

d.clear()
print(d)