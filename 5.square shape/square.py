import turtle

sk = turtle.Turtle()
sk.pensize(4)
sk.speed(1)

wn = turtle.Screen()
wn.bgcolor('yellow')

#create square
for i in range(4):
    sk.forward(200)
    sk.right(90)
turtle.done()