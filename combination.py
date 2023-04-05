n=input("Enter the number:")
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i!=j and j!=k and k!=i):
                print(n[i],n[j],n[k])
