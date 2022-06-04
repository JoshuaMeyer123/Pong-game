from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')


is_game_on = True
while is_game_on:
    scoreboard.update()
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect ball hitting walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # Detect ball hitting paddle
    if ball.distance(r_paddle) < 53 and ball.xcor() > 320 or ball.distance(l_paddle) < 53 and ball.xcor() < -320:
        ball.bounce_x()
        ball.faster()
    # Detect the ball missing the right paddle
    if ball.xcor() > 380:
        ball.screen_reset()
        scoreboard.l_score += 1
        ball.speed = 10
    # Detect the ball missing the left paddle
    if ball.xcor() < -380:
        ball.screen_reset()
        scoreboard.r_score += 1
        ball.speed = 10

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        is_game_on = False


screen.exitonclick()
