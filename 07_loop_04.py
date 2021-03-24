num = int(input("Enter Number: "))

for i in range(2,80):
    if num%i==0:
        print("It is Composite")
        break
    if num%i >0:
        print("It is Prime")
        break