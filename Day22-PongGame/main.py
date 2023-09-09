from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

P1 = Paddle((350, 0))
P2 = Paddle((-350, 0))
B1 = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(P1.up, "Up")
screen.onkey(P1.down, "Down")
screen.onkey(P2.up, "w")
screen.onkey(P2.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    B1.move()
    if B1.ycor() > 280 or B1.ycor() < - 280:
        B1.bounce_y()

    if B1.distance(P1) < 50 and B1.xcor() > 320 or B1.distance(P2) < 50 and B1.xcor() < -320:
        B1.bounce_x()

    if B1.xcor() > 380:
        B1.reset_position()
        print(scoreboard.l_score)
        scoreboard.l_point()

    if B1.xcor() < -380:
        B1.reset_position()
        print(scoreboard.r_score)
        scoreboard.r_point()

    scoreboard.update_scoreboard()
    screen.update()

screen.exitonclick()
