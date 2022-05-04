print("Enter a Power of 2")
num=int(input())
n=1
if num >= 0 and num < 31:
    for i in range(num):
        n=n*2
        print(n)
else:
    print("Enter number between 0 to 30")