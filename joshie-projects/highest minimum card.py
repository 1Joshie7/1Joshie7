a = int(input("enter a card number between o to 101"))
b = int(input("pick a second card"))
if a == 100:
    print("you have picked highest card", a)
elif b > a :
    print("the second card is now the highest card", b)
else:
    print("the highest card is ", a)

c = int(input("enter card"))
if c == 1:
    print("the minimum card is ", c)
elif b < c:
    print("the minimum card is ", b)
else:
    print("the minimum card is ", c)




