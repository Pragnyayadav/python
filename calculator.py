function = input("Enter what you want to do(Add/Subtract/Divide/Multiply): ")
function=function.lower()

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if("add" in function):
    print(a+b)
elif("subtract" in function):
    print(a-b)
elif("divide" in function):
    print(a/b)
elif("multiply"):
    print(a*b)
else:
    print("Cant calculate")