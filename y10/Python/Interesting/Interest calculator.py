print("Postive compounding multipication calculator")

#Data input
orignal_money = int(input("How much money do you have originally (Only Numbers)? "))
interest_factor = 1+(int(input("What percent is the interest per anum "))/100)
iterations = int(input("How many years do you want to calculate "))
current_money = orignal_money

#Calculation
for y in range(iterations):
    current_money = current_money*interest_factor
    print("In year", y+1)
    print("You will have", round(current_money, 2))