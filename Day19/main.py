
from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(500,400)

user_bet = screen.textinput("Which one will win??", prompt="What is your choice:")
colors = ['blue','orange','dark red','green','yellow','black']

all_turtle = []



Ypos = -110
offset =40

for Tur in range(len(colors)):
    tim = (Turtle(shape="turtle"))
    tim.penup()
    tim.color(colors[Tur])
    tim.goto(x=-230,y=(Ypos + offset))
    Ypos = Ypos + offset
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()> 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You are the winner")
            else:
                print(f"You've lost. The winner is {winner}")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


#tim = Turtle(shape="turtle")
#tim.penup()
#tim.goto(x=-230,y=-100)


#
#def move_forwards():
#    tim.forward(10)
#
#def move_backwards():
#    tim.backward(10)
#
#def turn_left():
#    tim.left(10)
#
#def turn_right():
#    tim.right(10)
#
#def clear():
#    tim.clear()
#    tim.penup()
#    tim.home()
#    tim.pendown()
#
#screen.listen()
#
#screen.onkey(move_forwards, "w")
#screen.onkey(move_backwards, "s")
#screen.onkey(turn_left, "a")
#screen.onkey(turn_right, "d")
#screen.onkey(clear, "c")
screen.exitonclick()


