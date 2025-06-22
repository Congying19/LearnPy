d={10:'cat',20:'dog',30:'zoo'}
print(d)

lst1=[10,20,30,40]
lst2=['cat','dog','zoo','mouze']
zipobj=zip(lst1,lst2)
print(zipobj)

#print(list(zipobj))
print(dict(zipobj))

print(max(d))
print(len(d))

t=(10,20,30)
d={t:10}
print(d)