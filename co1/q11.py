

a=int(input("enter the first number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
if(a>b and a>c):
    larg=a
elif(b>a and b>c):
    larg=b
else:
    larg=c
print("the largest number is",larg)
