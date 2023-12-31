import turtle
screen = turtle.Screen()
screen.setup(width=1.0,height=1.0)
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(100)
t.up()

#left decoration
for i in range(10):
    for i in range(2):
        t.pensize(6)
        t.goto(-450,25)
        t.down()
        t.color("")
        t.forward(25)
        t.circle(10,steps=4)
        t.right(15)
        t.color("lime")
        t.forward(25)
        t.right(120)
    t.right(30)
t.up()

#right decoration
for i in range(10):
    for i in range(2):
        t.pensize(6)
        t.goto(450,25)
        t.down()
        t.color("")
        t.forward(25)
        t.circle(10,steps=4)
        t.right(15)
        t.color("cyan")
        t.forward(25)
        t.right(120)
    t.right(30)
t.up()

#left decoration
for i in range(10):
    for i in range(2):
        t.pensize(6)
        t.goto(-600,300)
        t.down()
        t.color("deep sky blue")
        t.forward(50)
        t.circle(10,steps=4)
        t.right(15)
        t.color("dodger blue")
        t.forward(50)
        t.right(120)
    t.right(30)
t.up()

#right decoration
for i in range(10):
    for i in range(2):
        t.pensize(6)
        t.goto(600,300)
        t.down()
        t.color("brown")
        t.forward(50)
        t.circle(10,steps=4)
        t.right(15)
        t.color("maroon")
        t.forward(50)
        t.right(120)
    t.right(30)
t.up()

#left decoration
for i in range(10):
    for i in range(2):
        t.pensize(6)
        t.goto(-600,-250)
        t.down()
        t.color("tomato")
        t.forward(50)
        t.circle(10,steps=4)
        t.right(15)
        t.color("orange red")
        t.forward(50)
        t.right(120)
    t.right(30)
t.up()

#right decoration
for i in range(10):
    for i in range(2):
        t.pensize(6)
        t.goto(600,-250)
        t.down()
        t.color("violet")
        t.forward(50)
        t.circle(10,steps=4)
        t.right(15)
        t.color("fuchsia")
        t.forward(50)
        t.right(120)
    t.right(30)
t.up()

turtle.up()
turtle.color("deep pink")
turtle.goto(-300,200)
turtle.write("Happy",font=('Algerian',80,'italic','bold'))
turtle.goto(-150,50)
turtle.color("crimson")
turtle.write("New",font=('Algerian',80,'italic','bold'))
turtle.goto(0,-100)
turtle.color("fuchsia")
turtle.write("Year!!!",font=('Algerian',80,'italic','bold'))
turtle.goto(-150,-300)
turtle.color("gold")
turtle.write("2024",font=('Algerian',100,'italic','bold'))

turtle.done()




