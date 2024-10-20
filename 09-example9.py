# Conditional statement

num = int(input("Enter number (0 ~50): "))
if 50 >= num >= 40:
    print ("S")
elif 40 > num >= 30:
    print("A")
elif 30 > num > 20:
    print("B")
elif num == 20:
    print("E")
elif 20 > num >= 0:
    print("U")
else:
    print("Enter a valid number betwen 0 and 50")