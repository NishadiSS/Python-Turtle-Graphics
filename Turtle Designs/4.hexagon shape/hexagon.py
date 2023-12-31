#python program to draw hexagon using turtle programming

import turtle
polygon = turtle.Turtle()

num_of_sides = 6
side_length =80
angle = 360.0 / num_of_sides

for i in range(num_of_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()