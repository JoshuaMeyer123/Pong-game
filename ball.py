from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial'


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_dir = 1
        self.x_dir = 1
        self.ball_speed = 10

    def move(self):
        new_x = self.xcor() + self.ball_speed*self.x_dir
        new_y = self.ycor() + self.ball_speed*self.y_dir
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_dir = self.y_dir * -1

    def bounce_x(self):
        self.x_dir = self.x_dir * -1

    def screen_reset(self):
        self.goto(0, 0)
        self.x_dir = self.x_dir * -1

    def faster(self):
        self.ball_speed += 2
