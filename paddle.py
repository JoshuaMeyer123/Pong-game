from turtle import Turtle

MOVE = 20


class Paddle(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.setpos(coordinate)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)

    def move_up(self):
        current_pos = self.ycor()
        self.goto(self.xcor(), y=current_pos + MOVE)

    def move_down(self):
        current_pos = self.ycor()
        self.goto(self.xcor(), y=current_pos - MOVE)


