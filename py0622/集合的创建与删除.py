#直接创建
s={10,20,30,40,50}
print(s)
#使用set创建
s2=set()
print(s2)
print(bool(s2))
s3=set('helloworld')
print(s3)
s4=set([10,20,30,40])
print(s4)
s5=set(range(1,10))
print(s5)
#集合也是序列
print('s5最大值',max(s5))
print('1在s5里面',(1 in s5))