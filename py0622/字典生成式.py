import random
d={item : random.randint(a=1,b=100) for item in range(4)}
print(d)

lst1=[1001,1002,1003,1004]
lst2=['Jack','Marl','nb','oooo']
d={key:value for key,value in zip(lst1,lst2)}
print(d)