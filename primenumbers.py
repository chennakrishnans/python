M=int(input("Enter the value:"))
N=int(input("Enter the value:"))
print("Prime numbers between",M, "and" ,N, "are:")
for num in range (M,N+1):
    if num>1:
        for i in range(2,int(num/2)+1):
            if (num*i)==0:
                break
        else:
            print(num,end=",")
