from turtle import Turtle

STEP_SIZE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.penup()
        if position == "right":
            self.setx(350)
        elif position == "left":
            self.setx(-350)
        self.color("orangered2")

    def up(self):
        """Move the paddle up"""
        if self.ycor() < 250:
            new_y = self.ycor() + STEP_SIZE
            self.sety(new_y)

    def down(self):
        """Move the paddle down"""
        if self.ycor() > -230:
            new_y = self.ycor() - STEP_SIZE
            self.sety(new_y)
