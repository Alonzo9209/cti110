#Alonzo Aldape
#3/1/25
#P1HW2
#The goal is to be able to make a code like the picture example and you must be able to input different values and get results that work.

#print title 
print("This program calculates and displays travel expenses")
print()

#Get user input for each integer 
budget = int(input("Enter Budget: "))
print()

dest = input("Enter your travel desination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))
print()

hotel = int(input("Approximately, how much will you need for the accomodation/hotel? "))
print()

food = int(input("Last, how much do you need for food? "))
print()

print("------------Travel Expenses------------")

#Print results from above
print("Location: ", dest)

print("Initial Budget: ", budget)
print()

print("Fuel: ", gas)

print("Accomodation: ", hotel)

print("Food: ", food)
print()

#Calculate remaaining balance
result = budget - gas - hotel - food

#Run program to get results
print("Remaining Balance: ", result)
