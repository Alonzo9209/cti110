# Alonzo Aldape
# 3/9/25
# P2LAB1
# Create a program that can solve a circle radius and other inputs, it must be interchangable so it works with different values and always be true
import math


radius = float(input("Enter the radius: "))
print()
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

print(f"The diameter of the circle is {diam:.1f}")
print()

print(f"The circumference of the circle is {cir:.2f}")
print()

print(f"The area of the circle is {area:.3f}")
      
