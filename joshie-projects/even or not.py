a = int(input("enter a number"))
if (a<1) or (a>20):
    print("number must be between 0 and 21")
elif a % 2 == 0:
    print("number is even")
else:
    print("number is not an even number")