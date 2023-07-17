from turtle import*
from time import*
title("ainmation")
bgcolor("black")
pencolor("blue")
width(3)
speed(0)
sleep(2)

def flower(x):
    circle(100, x)
    penup()
    goto(0,0)
    pendown()
    circle(-100, x)

def leaf():
    for i in range(0,95,7):
        flower(i)
leaf()
setheading(50)
leaf()
setheading(100)
leaf()
setheading(150)
leaf()
setheading(200)
leaf()
setheading(250)
leaf()
setheading(300)
leaf()
setheading(350)
done()
