name = input("Enter your name :")
str = "Hello {}, How are you?"
if len(name) > 3:
    print(str.format(name))
else : 
    print("Please Enter Valid Name")