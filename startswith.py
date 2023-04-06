n=input("Enter the sentence:")
words=n.split(".")
count=0
for i in words:
    if i.startswith("B") or i.startswith("b"):
        count=count+1
print(count)
