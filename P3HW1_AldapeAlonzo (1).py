# Alonzo Aldape
# 3/30/25
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1 : "))
mod_2 = float(input("Enter grade for Module 2 : "))
mod_3 = float(input("Enter grade for Module 3 : "))
mod_4 = float(input("Enter grade for Module 4 : "))
mod_5 = float(input("Enter grade for Module 5 : "))
mod_6 = float(input("Enter grade for Module 6 : "))


# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# TO DO: determine lowest, highest , sum and average for grades


low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)


print("---------Results------------")
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average: {avg:.2f}")
print("--------------------------------------")


average = (mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6) / 6
# determine letter grade for average

if average >= 90:
    print('Your grade is: A')

elif average >= 80:
    print('Your grade is: B')

elif average >= 70:
    print('Your grade is: C')

elif average >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F') # TO DO: finish this
    



