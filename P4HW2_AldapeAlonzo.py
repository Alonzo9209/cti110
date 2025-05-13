# Alonzo Aldape
# 4/13/25
# P4HW2
# Make a code that can calculate hours/pay and can even include overtime to give you a gross pay number

#Pseudocode
#1.)First we ask the user to input their name or Done, it has to be captial or it will not stop the loop
#2.)we also ask them how many hours they work and how much they are paid
#3.)we determine if they have overtime by using if to see if hours inputed are over 40 if not there is no overtime
#4.)the code then calculates how much the person made in their check and how much of it came from over time and what is grosspay
#5.)results are then displayed to show the person who entered info to see how much they should except from next check
#6.)repeat step 1 again but we are looking for Done to break the loop since it's the only thing that would get us out otherwise another name would repeat everything
#7.)when Done is used it displays the total of how many people there are and all the pay and hours added up and program ends

num_employees = 0
reg_pay_total = 0
overtime_total = 0
gross_pay_total = 0

name = input("Enter employee's name or 'Done' to terminate: ")

while name != 'Done':
    hours = float(input("Enter number of hours worked: ")) 
    rate = float(input("Enter employee's pay rate: "))

    if hours > 40:
        overtime = hours - 40
        overtime_pay = overtime * rate * 1.5
        reg_pay = 40 * rate  
    else:
        overtime = 0
        overtime_pay = 0
        reg_pay = hours * rate

    gross_pay = reg_pay + overtime_pay

    reg_pay_total += reg_pay
    overtime_total += overtime_pay
    gross_pay_total += gross_pay
    num_employees += 1

    print('-------------------------------------')

    print("Employee name:", name) 
    print()

    print('Hours Worked    Pay Rate    Overtime    OverTime Pay    RegHour Pay    Gross Pay')

    print('-----------------------------------------------------------------------------------------')

    print(f'{hours:.1f}{rate:15.1f}{overtime:15.1f}{overtime_pay:15.2f}{reg_pay:15.2f}{gross_pay:15.2f}')
    print()

    name = input("Enter employee's name or 'Done' to terminate: ")
    print()

print(f"Total number of Employees: {num_employees}")
print(f"Total amount paid for overtime: ${overtime_total:.2f}")
print(f"Total amount paid for regular hours: ${reg_pay_total:.2f}")
print(f"Total amount paid for gross: ${gross_pay_total:.2f}")


    
