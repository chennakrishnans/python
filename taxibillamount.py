a=(input("Enter the taxi no:"))
n=input("Enter the name:")
km=int(input("Enter the km travelled:"))
if(km<=1):
    rate=km*25
elif(km>1 and km<6):
    rate=km*18
elif(km>6 and km<12):
    rate=km*15
elif(km>12 and km<18):
    rate=km*20
elif (km>=18):
    rate=km*25
print ("\nTaxi no:",a,"\nName:",n,"\nkilometres travelled:",km,"\nBill amount:",rate)
