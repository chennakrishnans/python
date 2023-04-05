n=int(input("Enter the rows:"))
num=2
for i in range(n):
    for j in range(i+1):
        print (num,end=" ")
    print()
    num*=num
