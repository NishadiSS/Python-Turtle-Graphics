import turtle

#set the turtle screen and background color
screen = turtle.Screen()
screen.bgcolor("black")

#create new turtle
t = turtle.Turtle()
t.speed(0)

#set the fill color to red
t.fillcolor("red")
t.begin_fill()

#Draw the circle with a radius of 100 pixels
t.circle(100)

#End the fill and stop drawing
t.end_fill()
t.hideturtle()

turtle.done()