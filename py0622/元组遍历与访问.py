t=('python','hello','world')
print(t[0])

t2=t[0:1:1]
print(t2)

t3=t[1:3:1]
print(t3)

#遍历的三种方法：
for item in t:
    print(item)

for i in range(0,len(t)):
    print(i,t[i])

for index,item in enumerate(t):
    print(index,item)