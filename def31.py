a=int(input("enter more 2 digit number:"))
odd=0
even=0
while a>0:
    res=a%10
    a=a//10
    if res%2==0:
        even+=1
    else:
        odd+=1

print(f"Total odd number is {odd} and even number is {even}")
