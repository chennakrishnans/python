lowcount=0
upcount=0
num=0
while True:
    char=input("Enter a charecter:")
    if (char=='*'):
        break
    elif char.isupper():
        upcount+=1
    elif char.islower():
        lowcount+=1
    elif char.isnumeric():
        num+=1
print("Total count of lower case:",lowcount)
print("Total count of upper case:",upcount)
print("Total count of numbers:",num)
