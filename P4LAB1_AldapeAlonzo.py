# Alonzo Aldape
# 4/6/25
# P4LAB1
#use turtle to draw triangle inside square

import turtle

# create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()


# Set Turtle options

pen.pensize(5)
pen.pencolor("green")
pen.shape("arrow")

#code to draw
for i in range(4):
    pen.forward(100)
    pen.left(90)

#loop 3 times

sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

#wait for user to close window
win.mainloop()
