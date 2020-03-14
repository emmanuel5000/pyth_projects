from random import randint

def checkit(x):
    zindex = 0
    oindex = 1
    numberofplayer = len(x)

    for f in range(0,numberofplayer):
        for s in range(0,len(x[f])):
            if int(x[f][s]) == 1 and int(x[f][s+1])==0:
                x.remove(x[f][s+1])
                x.remove(x[f][s])
                x[f].append("10")



                
            
def fixten(players,hands):
    for i in range(players-1):
        if hands[i] == '1' and hands[i+1] == '0':
            hands[i] == '10'
            hands.remove('0')

def endinghand(playernum,x):
    totalhand = 0
    for i in range(1,len(x[playernum])):
                   totalhand = totalhand +x[playernum][i]
    print('hand value is: '+ str(totalhand))
    if totalhand> 21:
        print('bust')
    if totalhand ==  21:
        print('winner')
                   
                   
    
            
def askplayer(playernum,x):
    total_hand_value = x[playernum][1] + x[playernum][2]
    print('Player '+str(playernum+1)+' hand a hand total of: ' +str(total_hand_value))
    
    if x[playernum][1] == 1:
        yesorno = input('enter y to inscrease your 1 to 11')
        if yesorno.lower() == 'y':
            x[playernum][1] = 11
    if x[playernum][2] == 1:
        yesorno = input('enter y to inscrease your 1 to 11')
        if yesorno.lower() == 'y':
            x[playernum][2] = 11
    
    while total_hand_value < 21:
        hit = input('enter to h to get a card,current hand: '+str(total_hand_value)+'\nenter d to stay')
        x[playernum].append(randint(1,10))
        total_hand_value = x[playernum][-1] + total_hand_value
        if hit=='d':
            break
    
            
