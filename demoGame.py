#pong games

import turtle

wn = turtle.Screen()
wn.title("Pong game by Nitesh")
wn.bgcolor("grey")
wn.setup(width=800,height=600)
wn.tracer(0)

# side bar A
sidebar_A = turtle.Turtle()
sidebar_A.speed(0)
sidebar_A.shape("square")
sidebar_A.color("white")
sidebar_A.shapesize(stretch_wid=5,stretch_len=1)
sidebar_A.up()
sidebar_A.goto(-350,0)

# side bar B

sidebar_B = turtle.Turtle()
sidebar_B.speed(0)
sidebar_B.shape("square")
sidebar_B.color("white")
sidebar_B.shapesize(stretch_wid=5,stretch_len=1)
sidebar_B.up()
sidebar_B.goto(350,0)

# BAll

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.shapesize()
Ball.up()
Ball.goto(0,0)

# ball moves by 2 pixels
Ball.dx = 2
Ball.dy = 2



# Functions to move side bars

def sidebar_A_up():
    y = sidebar_A.ycor()
    y += 20
    sidebar_A.sety(y)

def sidebar_A_down():
    y = sidebar_A.ycor()
    y -= 20
    sidebar_A.sety(y)


def sidebar_B_up():
    y = sidebar_B.ycor()
    y += 20
    sidebar_B.sety(y)

def sidebar_B_down():
    y = sidebar_B.ycor()
    y -= 20
    sidebar_B.sety(y)


# key press or key binding

wn.listen()
wn.onkey(sidebar_A_up,"w")
wn.onkey(sidebar_A_down,"s")
wn.onkey(sidebar_B_up,"Up")
wn.onkey(sidebar_B_down,"Down")









#Making Loop in the game
while True:
    wn.update()
    # move ball in game
  
    Ball.setx(Ball.xcor()+ Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #check if border hits the border

    

