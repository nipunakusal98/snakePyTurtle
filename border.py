import turtle

win=turtle.Screen()
win.bgcolor("lightblue")
#Draw Border
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
