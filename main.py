# Optional:
# Only required on certain Windows installations.

# import os
# os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
# os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'

import turtle as turtle_module
import random

DOT_SIZE = 20
DOT_SPACING = 50
GRID_SIZE = 10
START_OFFSET = 250

turtle_module.colormode(255)
timmy_the_turtle = turtle_module.Turtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()

# Extracted color palette inspired by Damien Hirst artwork
color_list = [(245, 243, 239), (247, 242, 245), (204, 165, 107), (239, 246, 241), (237, 240, 245), (155, 73, 46), (174, 154, 37), (51, 93, 124), (224, 201, 133), (139, 31, 20), (132, 163, 185), (201, 90, 69), (46, 123, 86), (13, 100, 73), (70, 48, 39), (99, 72, 74), (147, 179, 146), (235, 175, 164), (163, 141, 158), (55, 46, 50), (184, 206, 171), (18, 85, 90), (147, 18, 22), (41, 61, 74), (80, 146, 128), (187, 83, 87), (41, 66, 88), (108, 126, 151), (15, 72, 69), (175, 192, 213)]

timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(START_OFFSET)
timmy_the_turtle.setheading(0)
number_of_dots = GRID_SIZE * GRID_SIZE

for dot_count in range(1, number_of_dots + 1):
    timmy_the_turtle.dot(DOT_SIZE, random.choice(color_list))
    timmy_the_turtle.forward(DOT_SPACING)

    if dot_count % GRID_SIZE == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(DOT_SPACING)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(DOT_SPACING * GRID_SIZE)
        timmy_the_turtle.setheading(0)


screen = turtle_module.Screen()
screen.title("Hirst Painting Generator")
screen.exitonclick()
