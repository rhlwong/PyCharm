import random
from turtle import Turtle, Screen
import turtle
from random import randrange, randint


myTurtle = Turtle()
myTurtle.shape("turtle")
myTurtle.color("DodgerBlue3")

size = []

colors = ['blue','magenta','dark red','gold','honeydew','lime green','black']
angle = [0,90,180,270]
#for i in range(3,11):
#    size.append({'shape':i, 'angle':360/i})

#for s in size:
#    for _ in range(0,s['shape']):
#        myTurtle.forward(100)
#        myTurtle.right(s['angle'])



myTurtle.pensize(1)
turtle.colormode(255)
myTurtle.speed(0)
for _ in range(90):
    randColor = (randint(1,255),randint(1,255),randint(1,255))
    myTurtle.pencolor(randColor)
    myTurtle.circle(120)
    myTurtle.setheading(myTurtle.heading()+15)






myScreen = turtle.Screen()
myScreen.exitonclick()
