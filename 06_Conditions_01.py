num1 = input("Enter: ")
num2 = input("Enter: ")
num3 = input("Enter: ")
num4 = input("Enter: ")

if (num1 > num2 and num1 > num3 and num1 > num4):
    print(num1)
elif(num2 > num3 and num2 > num4):
    print(num2)
elif(num3 > num4):
    print(num3)
else:
    print(num4)