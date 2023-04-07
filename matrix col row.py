a=[[3,4,5],[7,8,9],[10,11,121]]
print (a)
row_sum=[0]*len(a)
col_sum=[0]*len(a[0])
diag_sum=0
for i in range (len(a)):
    for j in range(len (a[0])):
        row_sum[i]+=a[i][j]
        col_sum[j]+=a[i][j]
        if i==j:
            diag_sum+=a[i][j]
print(row_sum)
print(col_sum)
print(diag_sum)
