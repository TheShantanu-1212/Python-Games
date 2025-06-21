from turtle import Turtle
import random

BASE_SPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("paleturquoise")
        self.penup()
        self.setheading(120)
        self.move_speed = BASE_SPEED
        self.move()

    def move(self):
        """Move the ball forward"""
        self.forward(self.move_speed)

    def wall_bounce(self):
        """Simulate bouncing off the wall"""
        self.setheading(-self.heading())

    def paddle_bounce(self):
        """Simulate bouncing off a paddle"""
        self.setheading(-self.heading() - 180)
        self.move_speed += 0.1

    def reset(self):
        """Reset the ball after a player scores"""
        self.move_speed = BASE_SPEED
        if self.xcor() > 350:
            self.setheading(random.randint(120, 240))
        else:
            self.setheading(random.randint(-60, 60))
        self.goto(0, 0)
        self.move()
