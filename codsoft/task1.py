#  Making Calculator for Codsoft internship:
print("WELCOME")
a=float(input("Enter the first number"))
b=float(input("Enter the second number"))
c=input("please press'+', '-', '*', '/','^',")
if c=='+':
    print("The answer is:",a+b)
elif c=='-':
    print("The answer is:",a-b)
elif c=='*':
    print("The answer is:",a*b)
elif c=='/':
    print("The answer is:",a/b)
elif c=='**':
    print(a**b)
else:
    print(" The operation is invalid")
