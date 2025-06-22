d={1:'hello',2:'world',3:'你好',4:'世界'}
print(d)

print(d[1])
print(d.get(2))
print(d.get(5,'not exist'))

for item in d.items():
    print(item)
for key,value in d.items():
    print(key,':',value)