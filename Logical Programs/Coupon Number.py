import random

def couponNumber(N):
    count=0
    for i in range(500):
        randomNum=random.randint(1,100)
        if(randomNum==N):
            count+=1
        print("The coupon Number ", N ,"has repeated", count,"times")
N = int(input("Enter a Number :"))
couponNumber(N)        