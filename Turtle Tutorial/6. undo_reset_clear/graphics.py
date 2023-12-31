#Undo() -> Reverses the most recent drawing action-Last drawing command
#Clear() -> Erases all drawings- Drawings only
#Reset() -> Erases drawings and resets turtle attributes - 

import turtle
t = turtle.Turtle()

t.circle(100)
t.circle(-100)
t.undo()
t.undo()

t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.undo()
t.undo()
t.undo()
t.undo()
t.undo()

t.backward(100)
t.right(90)
t.forward(100)
t.clear()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.reset()