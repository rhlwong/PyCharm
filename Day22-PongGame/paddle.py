from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)
        self.color("white")

    def up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(),self.new_y)

    def down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(),self.new_y)