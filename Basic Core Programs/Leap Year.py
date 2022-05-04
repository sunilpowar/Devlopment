year = int(input("Enter Year :"))
if year < 1000 or year > 9999:
    print("Please Enter Valid Year")
elif (year % 4 == 0):
    print("This is Leap Year")
else:
    print("This is not Leap Year")
    