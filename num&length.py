#exercise 1
integer=int(input("enter a number"))
length=int(input("enter a length"))
i=1
result=[]
while length>=i:
    result.append(i*integer)
    i=i+1
print(result)
#exercise 2
word=input("enter a word")
modifiedstring=""
for char in word:
    if not modifiedstring or char !=modifiedstring[-1]:
        modifiedstring+=char
print(modifiedstring)
