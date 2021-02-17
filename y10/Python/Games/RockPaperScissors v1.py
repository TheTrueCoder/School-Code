import os

#Define functions
def clear(): os.system('cls') #Clear shell on Windows System
def checkAttack(attack, enemyAttack):
    if killsWhat[attack] == enemyAttack:
        return True
    else: return False

#Game data
weaponNames = ["Rock", "Paper", "Scissors"]
killsWhat = [2, 0, 1]

clear()
while True:
    games = int(input("How many rounds of Rock Paper Scissors do you want to play? "))
    for game in range(games):
        print("It's player 1's turn. Don't look player 2. 1 is Rock, 2 is Paper and 3 is Scissors.")
        p1Weapon = int(input("Player 1, Choose your weapon! "))-1
        clear()
        
        print("It's player 2's turn. Don't look player 1. 1 is Rock, 2 is Paper and 3 is Scissors.")
        p2Weapon = int(input("Player 2, Choose your weapon! "))-1
        clear()

        if checkAttack(p1Weapon, p2Weapon) == True: winner = 1
        elif checkAttack(p2Weapon, p1Weapon) == True: winner = 2
        else: winner = 0

        if winner == 0:
            print("It's a draw.")
        else:
            print("Player {} won!".format(winner))
    if input("Do you want to start again? y/n ") == "n":
        exit
