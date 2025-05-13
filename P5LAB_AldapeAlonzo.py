#Alonzo Aldape
#4/20/25
#P5LAB
#The goal of this lab is to build a program that will generate a random amount of money owed and you can then calculate how much change is needed based on how much you give to pay the amount.

import random

def disperse_change(change):


    change = round(change* 100)


    #how many dollars
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    #how many quarters
    num_quarters = change // 25
    change = change - (num_quarters * 25)

    #how many dimes
    num_dimes = change // 10
    change = change - (num_dimes * 10)

    #how many nickels
    num_nickels = change // 5
    change = change - (num_nickels * 5)

    #how many pennies
    num_pennies = change 





#display coins needed
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
       if num_nickels == 1:
            print(f"{num_nickels} Nickel")
       else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")

def main():

    #logic for generator
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    #how much customer will pay you
    money_in = float(input("How much cash will you put in the self-checkout? "))

    #how much they get back
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    disperse_change(change)

main()
