marks1 = int(input("Enter Marks: "))
marks2 = int(input("Enter Marks: "))
marks3 = int(input("Enter Marks: "))
marks4 = int(input("Enter Marks: "))

if(marks1<33 or marks2<33 or marks3<33 or marks4<33):
    print("Fail ho gye tum BC")
elif(marks1+marks2+marks3+marks4 < 160):
    print("Tum fail ho gye BC")
else:
    print("Tu pass ho gya, Party de")