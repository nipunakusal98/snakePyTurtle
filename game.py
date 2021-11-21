import turtle
import time
import random


#time delay
delay=0.1


#Score
score=0
high_score=0


#screen setup
wn=turtle.Screen()#screen
wn.title("game by LemOnHerO")
wn.bgcolor("green")#background color
wn.setup(width=500,height=500)#screen size in pixels
wn.tracer(0)# cancels animation....turns off screen updates

#Draw Border
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-335,-335)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(670)
    mypen.left(90)
mypen.hideturtle()

#creating the snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction="stop"


#snake egg
egg=turtle.Turtle()
egg.speed(0)
egg.shape("circle")
egg.color("red")
egg.penup()
egg.goto(0,150)



#Snake Body(segments)

segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,230)
pen.write("Score:0 High Score:0", align="center", font=("courier", 24, "normal"))


#Functions
#move
def move():
    if head.direction == "up":
        y=head.ycor()# y coordinate
        head.sety(y+20)
        
    if head.direction == "down":
        y=head.ycor()# y coordinate
        head.sety(y-20)

    if head.direction == "left":
        x=head.xcor()# x coordinate
        head.setx(x-20)

    if head.direction == "right":
        x=head.xcor()# x coordinate
        head.setx(x+20)

def go_up():
    if head.direction != "down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"


#Key Binds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game Loop
while True:
    wn.update()


#collision with the boundery
    if head.xcor()>300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #Clear segments
        segments.clear()

        #reset score
        score=0
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score), align="center", font=("courier", 24, "normal"))

#collition with the egg
    if head.distance(egg)<20:
    #move the egg to a random place
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        egg.goto(x,y)
        
        #Add a new segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -=0.001

        #increase score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score), align="center", font=("courier", 24, "normal"))

    #move the end segment first in reverse
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
        if len(segments)>0:
            x=head.xcor()
            y=head.ycor()
            segments[0].goto(x,y)
            


    
    move()

    #check for head collisions with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segment list
            segments.clear()

            #reset score
            score=0
            pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score), align="center", font=("courier", 24, "normal"))
    
    time.sleep(delay)


wn.mainloop()#keep the window open for us.
