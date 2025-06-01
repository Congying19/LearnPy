a=100 # 变量a 值为100
b=50 #变量b 值为50
print(a) #输出变量值
print(90)#输出90
print(a*b) #输出运算结果

print('a')
print(a,b,'abc')
print(chr(98))
print(ord('彭'))
print(chr(24429))
fp=open("note.txt",'w')
print("abcdefg",file=fp)
fp.close()
print('a' , end='--')
print('b')
print('a','b',end='--',sep='/')
print('abc'+'edf')