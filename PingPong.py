 #pong games

import turtle
import time

wn = turtle.Screen()
wn.title("Pong game by Nitesh")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Side bar  A
sidebar_A = turtle.Turtle()
sidebar_A.speed(0)
sidebar_A.shape("square")
sidebar_A.color("white")
sidebar_A.shapesize(stretch_wid=5,stretch_len=1)
sidebar_A.penup()
sidebar_A.goto(-350, 0)

# Side Bar B
sidebar_B = turtle.Turtle()
sidebar_B.speed(0)
sidebar_B.shape("square")
sidebar_B.color("white")
sidebar_B.shapesize(stretch_wid=5,stretch_len=1)
sidebar_B.penup()
sidebar_B.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def sidebar_a_up():
    y = sidebar_A.ycor()
    y += 20
    sidebar_A.sety(y)

def sidebar_A_down():
    y = sidebar_A.ycor()
    y -= 20
    sidebar_A.sety(y)

def sideba_b_up():
    y = sidebar_B.ycor()
    y += 20
    sidebar_B.sety(y)

def sidebar_b_down():
    y = sidebar_B.ycor()
    y -= 20
    sidebar_B.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(sidebar_a_up, "w")
wn.onkeypress(sidebar_A_down, "s")
wn.onkeypress(sideba_b_up, "Up")
wn.onkeypress(sidebar_b_down, "Down")

# Main game loop
while True:
    wn.update()
    time.sleep(1/100)
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
  
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
  

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < sidebar_A.ycor() + 50 and ball.ycor() > sidebar_A.ycor() - 50:
        ball.dx *= -1 
  
    
    elif ball.xcor() > 340 and ball.ycor() < sidebar_B.ycor() + 50 and ball.ycor() > sidebar_B.ycor() - 50:
        ball.dx *= -1
  