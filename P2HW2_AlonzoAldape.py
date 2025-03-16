#Alonzo Aldape

#3/16/25

#P2HW2

#Using lists to make a grade calculator that works with different numbers in it



module_grades = []

mod1 = float(input("Enter grade for Module 1 : "))
module_grades.append(mod1)

mod2 = float(input("Enter grade for Module 2 : "))
module_grades.append(mod2)

mod3 = float(input("Enter grade for Module 3 : "))
module_grades.append(mod3)

mod4 = float(input("Enter grade for Module 4 : "))
module_grades.append(mod4)

mod5 = float(input("Enter grade for Module 5 : "))
module_grades.append(mod5)

mod6 = float(input("Enter grade for Module 6 : "))
module_grades.append(mod6)

print()
print("------------Results--------------")

min_value = min(module_grades)
max_value = max(module_grades)
average = sum(module_grades) / 6
total = sum(module_grades)

print(f"{"Lowest Grade:":<20} {min_value:<10}")
print(f"{"Highest Grade:":<20} {max_value:<10}")
print(f"{"Sum of Grades:":<20} {total:<10}")
print(f"{"Average:":<20} {average:<10.2f}")

print("----------------------------------")
