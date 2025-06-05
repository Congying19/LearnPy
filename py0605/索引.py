s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='   ')
print('_'*20)
for i in range(-len(s),0):
    print(i,s[i],end='   ')
print("_"*20)
print(s[0:5:2])
print(s[::-1])
print(s[:4:-2])
print(s.count('l'))
