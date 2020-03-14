#black the jack
from random import randint
from mmm import fixten
from mmm import askplayer
from mmm import endinghand


numplayers = 0
while numplayers <=1:
    numplayers = int(input("enter number of players \n"))
    if(numplayers>=1):
        break
#list format (player, card,more cards..)

print("handing out hands for: "+str(numplayers)+" players")
playerset = [1]
for i in range(2,numplayers+1):
             
             playerset.append(i)

print(playerset)


for i in range(0,numplayers):
    playerset[i] = [i+1,randint(1,10),randint(1,10)]

 
fixten(len(playerset),playerset)
#print(playerset[0][0].index("1"))
print(playerset)


for i in range(0,numplayers):
    askplayer(i,playerset)
    print('\n')

for i in range(0,numplayers):
    endinghand(i,playerset)
    print('\n')

print(playerset)
