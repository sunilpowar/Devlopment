import random
def flipCoin(N):
    heads = 0
    tails = 0
    hpercent = 0
    tpercent = 0
    for i in range (0,N) :
        Coin = random.random()
        print(Coin)
        if(float(Coin) < 0.5):
            heads += 1
        else:
            tails += 1
    hpercent = (heads/N) * 100
    tpercent = (tails/N) * 100
    print("Percentage of tail over head is {}".format(hpercent))
    print("Percentage of head over tail is {}".format(tpercent))
N = int(input("Enter the number to flip coin :"))
flipCoin(N)

            

 
  

 
            
            
   
        