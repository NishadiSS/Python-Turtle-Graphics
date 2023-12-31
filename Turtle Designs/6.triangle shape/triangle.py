import turtle

#set the new screen and background color
screen =turtle.Screen()
turtle.bgcolor("yellow")

#set the fill color for the triangle
turtle.fillcolor("green")
turtle.begin_fill()
turtle.pendown()

#Draw the 3 sides of the triangle
for i in range(3):
    turtle.forward(300)
    turtle.left(120)
turtle.end_fill()

turtle.done()