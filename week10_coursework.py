import random
#Class:
class Die:
    """create a class Die that simulate a die rolling"""
    def __init__(self):
        self.die=1

    def rollDie(self):
        self.die=random.randint(1,6)

    def getDie(self):
        return self.die

class Player:
    """store the name of the player, the score of the player and the sum of the player"""
    def __init__(self,name):
        self._name=name
        self.score=0
        self.sum_score=0

    def updateScore(self,dice1,dice2):
        if dice1==dice2 and dice1==4:
            self.score=-5
        elif dice1==dice2 and dice1!=4:
            self.score=dice1*4
        else:
            self.score=dice1+dice2
    
    def sumAllScore(self):
        self.sum_score=self.score+self.sum_score

    def getName(self):
        return self._name

    def getUpdateScore(self):
        return self.score

    def getSum(self):
        return self.sum_score
#************************************************************************
#Function:
def gameOver(player1,player2):
    sum1=int(player1.getSum())
    sum2=int(player2.getSum())
    if sum1 >=50 or sum2 >=50:
        return True
    else:
        return False

def castDice(dice1,dice2):
    dice1.rollDie()
    dice2.rollDie()
    return dice1.getDie(),dice2.getDie()
 
def displayWinner(player1,player2):
    sum1=player1.getSum()
    sum2=player2.getSum()
    if sum1>50 and sum2<50:
        print(player1.getName(), "is winner!!!")
    elif sum2>50 and sum1<50:
        print(player2.getName(), "is winner!!!")
    elif sum1>50 and sum2>50:
        print(player1.getName(), "is winner!!!")
#************************************************************************
#main program
name_P1=input("Please input the name of Player 1:")
name_P2=input("Please input the name of Player 2:")
dice1=Die()
dice2=Die()
player1=Player(name_P1)
player2=Player(name_P2)

while not gameOver(player1,player2):
    #Player1:
    die1,die2=castDice(dice1,dice2)
    player1.updateScore(die1,die2)
    player1.sumAllScore()
    print("Die 1-->{x}        Die 2-->{y}".format(x=die1,y=die2))
    if die1==die2 and die1!=4:
        print("Congratulations! You gain double score of the current turn")
    
    #Player2:
    die1,die2=castDice(dice1,dice2)
    player2.updateScore(die1,die2)
    player2.sumAllScore() 
    print("Die 1-->{x}        Die 2-->{y}".format(x=die1,y=die2))
    if die1==die2 and die1!=4:
        print("Congratulations! You gain double score of the current turn")
   
    #Print two players score
    print("{x}'s update score:{y}      {x}'s sum score:{z}"\
        .format(x=player1.getName(),y=player1.getUpdateScore(),\
        z=player1.getSum()))
    print("{x}'s update score:{y}      {x}'s sum score:{z}"\
        .format(x=player2.getName(),y=player2.getUpdateScore(),\
        z=player2.getSum()))
    displayWinner(player1,player2)
