n=int(input("Enter the number:"))
oddsum=0
evensum=0
for i in range(1,n+1):
    a=int(input("Enter the elements:"))
    if a%2==0:
        evensum=evensum+a**2
    else:
        oddsum=oddsum+a**2
print("[",oddsum,",",evensum,"]")
