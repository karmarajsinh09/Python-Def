a=[3,1,2,3,4,3,2]
print(a)

f=int(input("Enter number that you want to find :"))
cnt=0
for i in a:
    if i==f:
        cnt+=1
    
if cnt>1:
    print(f"The number is {f} and it repeated {cnt} Times")
elif cnt==1:
    print(f"The Number {f} is not repeated")
elif cnt==0:
    print(f"The Number {f} is not in list")
