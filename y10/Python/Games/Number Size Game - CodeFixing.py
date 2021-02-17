import random

rounds = 3

print("Welcome to the number guess game")
print("I will show you two numbers")
print("You must tell me which is higher in level 1")
print("and which is lower in level 2")
print("You will need to get 10 correct to move on to the next level.")

name = input("What is your name? ")
print("Hello",name)

corrAnswers = 0
print("Level 1")

while corrAnswers < rounds:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    while True:
        try:
            userGuess = int(input("Which number is higher, {} or {}? ".format(num1,num2)))
            break
        except ValueError:
            print("Please input a whole number")

    correctAnswer = max(num1,num2)

    if userGuess == correctAnswer:
        print("Well done, that is correct!")
        corrAnswers += 1
    elif userGuess > 20:
        print("That is to big. (Over 20)")
    elif userGuess < 1:
        print("That is to low. (Under 1)")
    else:
        print("That's incorrect.")

print("Well done you made it to level 2!")
corrAnswers = 0
while corrAnswers < rounds:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    while True:
        try:
            userGuess = int(input("Which number is lower, {} or {}? ".format(num1,num2)))
            break
        except ValueError:
            print("Please input a whole number")

    correctAnswer = min(num1,num2)

    if userGuess == correctAnswer:
        print("Well done, that is correct!")
        corrAnswers += 1
    elif userGuess > 20:
        print("That is to big. (Over 20)")
    elif userGuess < 1:
        print("That is to low. (Under 1)")
    else:
        print("That's incorrect.")