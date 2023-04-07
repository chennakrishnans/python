a=input("Enter the string:")
b=sorted(a)
print (b)
count=0
for i in range(len(b)):
    if b[i]==b[i+1]:
        count+=1
        print(i)
        break
    else:
        continue
