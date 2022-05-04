def harmonicNo(n):
    num=0
    for i in range(1,n+1):
        num=num+1/i
        print(num)
n=int(input("Enter the Number : "))
harmonicNo(n)