import os
import random

#Define functions
def clear(): os.system('cls') #Clear shell on Windows System
def checkAttack(attack, enemyAttack):
    if killsWhat[attack] == enemyAttack:
        return True
    else: return False

#Game data
weaponNames = ["Rock", "Paper", "Scissors"]
killsWhat = [2, 0, 1]
winResponses = ["is the winner", "took the win", "got the dub", "deleted the opposition"]

#Clear Terminal for clean consistent look.
clear()

#Init vars
gameMode = False
p1TotalScore = 0
p2TotalScore = 0

if str(input("What game mode do you want? pvp or pvcpu? ")) == "pvp": gameMode = True

while True:
    games = int(input("How many rounds of Rock Paper Scissors do you want to play? "))
    for game in range(games):
        currentPlayer = 1
        if gameMode==True:
            print("It's player 1's turn. Don't look player 2. 1 is Rock, 2 is Paper and 3 is Scissors.")
            p1Weapon = int(input("Player 1, Choose your weapon! (Only numbers) "))-1
            clear()
            
            print("It's player 2's turn. Don't look player 1. 1 is Rock, 2 is Paper and 3 is Scissors.")
            p2Weapon = int(input("Player 2, Choose your weapon! (Only numbers) "))-1
            clear()
        else:
            print("It's your turn. 1 is Rock, 2 is Paper and 3 is Scissors.")
            p1Weapon = int(input("Player 1, Choose your weapon! (Only numbers) "))-1
            clear()

            p2Weapon = random.randint(0,2)

        print("Player 1 chose", weaponNames[p1Weapon])
        print("Player 2 chose", weaponNames[p2Weapon])

        if checkAttack(p1Weapon, p2Weapon) == True: winner = 1
        elif checkAttack(p2Weapon, p1Weapon) == True: winner = 2
        else: winner = 0

        if winner == 0:
            print("It's a draw.")
        elif winner == 1:
            print("Player {} won!".format(winner))
            p1TotalScore += 1
        else:
            print("Player {} won!".format(winner))
            p2TotalScore += 1
    if p1TotalScore == p2TotalScore:
        print("Overall, It's a draw.")
    elif p1TotalScore > p2TotalScore:
        print("Overall, Player 1 {}!".format(winResponses[random.randint(0,len(winResponses)-1)]))
    else:
        print("Overall, Player 2 {}!".format(winResponses[random.randint(0,len(winResponses)-1)]))

    if input("Do you want to start again? y/n ") == "n":
        exit
