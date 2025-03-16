#Alonzo Aldape
#3/1/25
#P2HW1
#The goal is to be able to make a code like the picture example and you must be able to input different values and get results that work.

#print title 
print("This program calculates and displays travel expenses")
print()

#Get user input for each integer 
budget = float(input("Enter Budget: "))
print()

dest = input("Enter your travel desination: ")
print()

gas = float(input("How much do you think you will spend on gas? "))
print()

hotel = float(input("Approximately, how much will you need for the accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))
print()

print("------------Travel Expenses------------")

#Print results from above
print(f"{"Location:":<20}{dest:<10}")

print(f"{"Initial Budget:":<20}${budget:<10.2f}")

print(f"{"Fuel:":<20}${gas:<10.2f}")

print(f"{"Accomodation:":<20}${hotel:<10.2f}")

print(f"{"Food:":<20}${food:<10.2f}")


budget2 = float(int(budget))
gas2 = float(int(gas))
hotel2 = float(int(hotel))
food2 = float(int(food))

balance = budget2 - gas2 - hotel2 - food2
print("--------------------------------------------")

print()

print(f"{"Remaining Balance:":<20}${balance:<10.2f}")


