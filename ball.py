from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def right_bounds(self):
        self.goto(x=0, y=0)
        self.paddle_bounce()
        self.move_speed = 0.1

    def left_bounds(self):
        self.goto(x=0, y=0)
        self.paddle_bounce()
        self.move_speed = 0.1
