def fact(a):
    if a<=1:
        return a
    else:
        a=a*fact(a-1)
    return a
    

f=int(input("Enter Number For Factorial :"))
print(fact(f))