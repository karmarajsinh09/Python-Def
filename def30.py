dict1={1:"abc",2:"def",3:"ghi",4:"jkl"}
print(dict1)

a=int(input("Enter key for remove value from dictionary:"))

print("Removed :",dict1.get(a))

del dict1[a]
a=str(a)
print(dict1)
