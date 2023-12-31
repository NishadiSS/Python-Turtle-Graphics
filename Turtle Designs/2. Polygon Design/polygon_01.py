import turtle 
my_shape = turtle.Turtle()

turtle.bgcolor("yellow") 
num_sides = 8
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides):
    my_shape.forward(side_length)
    my_shape.right(angle)
     
turtle.done()