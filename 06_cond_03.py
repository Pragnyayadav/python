msg = input("Enter the text: ")
msg = msg.lower()
if("make a lot of money" in msg):
    spam = True
elif("buy now" in msg):
    spam = True
elif("click this" in msg):
    spam =True
else:
    spam= False

if(spam == True):
    print("This is a Spam Message")
else:
    print("This isn't Spam Message")