import random

stake=int(input("Enter Stack Amount :"))
goal=int(input("Enter Goal Amount : "))
win=0
loss=0

while (stake>0 and stake<goal):
    gamble=random.randint(0,1)
    if gamble==0:
        stake-=1
        loss+=1
    else:
        stake+=1
        win+=1

winPercent=(win*100)/(win+loss)
lossPercent=(loss*100)/(win+loss)
        
print("Number of wins: ", win)
print("Win percentage : ", winPercent)
print("Loss Percentage :", lossPercent )

          
    