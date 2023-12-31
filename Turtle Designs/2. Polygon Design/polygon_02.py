import turtle
import colorsys

def draw_spiral(size, color):
    turtle.pencolor(color)
    for i in range(100):
        turtle.forward(size)
        turtle.right(45)
        size += 5

def create_rainbow_spirals():
    turtle.speed(0)
    turtle.bgcolor("black")

    for i in range(36):
        hue = i / 36.0
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        draw_spiral(1, color)

    turtle.hideturtle()
    turtle.done()

create_rainbow_spirals()