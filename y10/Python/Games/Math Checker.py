#Libraries
import random

#Lists
#answers = ["Addition","Subtraction","Multipication","Division"]
opwords = ["plus","minus","times","divided by"]
points = 0

numOfQs = int(input("How many questions do you want to do? "))

#Loop
for i in range(numOfQs):
    #Init
    qnum = random.randint(0,3)

    #Get numbers from user
    number1 = int(input("Pick a whole number: "))
    number2 = int(input("Pick another whole number: "))

    #Gets user's answer
    userAnswer = float(input("What is {} {} {}? ".format(number1,opwords[qnum],number2)))

    #Calculates correct answer
    if (qnum==0):
        correctAnswer = number1+number2
    elif (qnum==1):
        correctAnswer = number1-number2
    elif (qnum==2):
        correctAnswer = number1*number2
    else:
        correctAnswer = number1/number2


    #Responds to user
    if (userAnswer==correctAnswer):
        points += 1
        print("Well done, correct!")
    else:
        print("Incorrect. You better get it right next time!")

#End message
corrInRatio = points/numOfQs
if (corrInRatio > 0.5):
    print("Well done! You got {} out of {} questions right!".format(points,numOfQs))
else:
    print("Thank you for playing, but your skills could use some improvement. You got only got {} out of {} questions right.".format(points,numOfQs))