a=input("Enter s1:")
b=input("Enter s2:")
count=0
for i in range(min(len(a),len(b))):
    if(a[i]==b[j]):
       count+=1
print(count)
