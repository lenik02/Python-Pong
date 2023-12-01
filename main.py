from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = ScoreBoard()
screen.listen()

screen.onkeypress(right_paddle.go_up, key='Up')
screen.onkeypress(right_paddle.go_down, key='Down')

screen.onkeypress(left_paddle.go_up, key='w')
screen.onkeypress(left_paddle.go_down, key='s')

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #   Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    #   Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
    #   Ball out of right bounds
    if ball.xcor() > 400:
        ball.right_bounds()
        scoreboard.right_point()
    #   Ball out of left bounds
    if ball.xcor() < -400:
        ball.left_bounds()
        scoreboard.left_point()

screen.exitonclick()
