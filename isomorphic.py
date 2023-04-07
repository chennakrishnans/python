s=input("Enter the string:")
t=input("Enter the string:")
map1=[]
map2=[]
for i in s:
    map1.append(s.index(i))
for i in t:
    map2.append(t.index(i))
if map1==map2:
    print("True")
else:
    print("False")
