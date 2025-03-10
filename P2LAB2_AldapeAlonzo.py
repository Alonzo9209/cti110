# Alonzo Aldape
# 3/9/25
# P2LAB2
# This code is supposed to help you pick a car and it will explain the miles per gallon and will help you understand how good the car is for you.

cars = {'Camaro' :18.21, 'Prius' :52.36, 'Model S' :110, 'Silverado' :26}

cars_keys = cars.keys()

print(cars_keys)
print()

print(*cars_keys, sep = ", ")

car_name = input("Enter a car: ")
print()
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")
print()

miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

gallons_needed = miles_driven/car_mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
      



