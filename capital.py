a=input("Enter the sentence:")
words=a.split()
b=[word[0].upper () for word in words]
result=".". join(b)
print(result)
