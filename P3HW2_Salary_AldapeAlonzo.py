# Alonzo Aldape
# 3/30/25
# P3HW2
# Make a code that can calculate hours/pay and can even include overtime to give you a gross pay number

#Pseudocode
#1.)First we ask the user to input their name
#2.)we also ask them how many hours they work and how much they are paid
#3.)we determine if they have overtime by using if to see if hours inputed are over 40 if not there is no overtime
#4.)the code then calculates how much the person made in their check and how much of it came from over time and what is grosspay
#5.)results are then displayed to show the person who entered info to see how much they should except from next check


name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: ")) 
rate = float(input("Enter employee's pay rate: "))

print('-------------------------------------')

print("Employee name:", name) 
print()

print('Hours Worked    Pay Rate    Overtime    OverTime Pay    RegHour Pay    Gross Pay')

print('-----------------------------------------------------------------------------------------')

if hours > 40:
    overtime = hours - 40
    overtime_pay = overtime * rate * 1.5
    reg_pay = 40 * rate  
else:
    overtime = 0
    overtime_pay = 0
    reg_pay = hours * rate

gross_pay = reg_pay + overtime_pay

print(f'{hours:.1f}{rate:15.1f}{overtime:15.1f}{overtime_pay:15.2f}{reg_pay:15.2f}{gross_pay:15.2f}')
    
