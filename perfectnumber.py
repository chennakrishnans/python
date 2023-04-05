n=int(input("Enter the number: "))
sum=0
for i in range(1,n):
    if(n%i==0):
     sum=sum+i
if(sum==n):
    print ("The given number is perfect")
else:
    print ("The given number is not perfect")
