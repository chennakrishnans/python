n=int(input("Enter the number:"))
sum=0
pro=1
while(n>0):
    digit=n%10
    sum+=digit
    pro*=digit
    n=n//10
if (sum==pro):
    print("Yes")
else:
    print("No")
