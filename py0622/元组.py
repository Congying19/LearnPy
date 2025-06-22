t=('helloworld')
print(t)
t=('hello',50,'nb')
print(t)

t=tuple('helloworld')
print(t)

t=tuple([20,30,40,50])
print(t)

print('10在元组里面',(10 in t))
print('40不在元组里面',(40 not in t))
print('最大值',max(t))
print(t.index(20))
print(len(t))

