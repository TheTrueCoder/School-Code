#Libs
import random

#Parameters
targetScore = 21
roundFinishWord = "hold"

#Intro
print("Welcome to this multiplayer dice game!")
print("You get 2 dice to 'roll' and the aim of the game is to get as close to {} without going over.".format(targetScore))

#Init
playerScores = []
playerScoresDelta = []

#Setup questions
noOfPlayers = int(input("How many players do you have? "))

#Main loop
for player in range(noOfPlayers):
    roundTotal = 0
    turn = 1
    print("\nIt's Player {}'s turn.".format(player+1))
    while True:
        print("It's round {}.".format(turn))
        #Roll dice
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        rollTotal = die1+die2
        roundTotal += rollTotal

        #Tell player
        print("You rolled {} and {} (Roll total is {}). Your round total is {}.".format(die1,die2,rollTotal,roundTotal))

        if roundTotal > targetScore or input("Do you want to roll or hold? ") == roundFinishWord:
            break
        else:
            turn += 1
    print("You got {} points.".format(roundTotal))
    playerScores.insert(player, roundTotal)
    playerScoresDelta.insert(player, targetScore - roundTotal)

#Check scores
winPlayer = playerScoresDelta.index(max(playerScoresDelta))+1
print("\nWell done player {}, You won!".format(winPlayer))