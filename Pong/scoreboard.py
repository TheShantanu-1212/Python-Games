from turtle import Turtle

FONT = ("JetBrainsMono", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-100, 220)
        self.right_score = 0
        self.left_score = 0
        self.color("slateblue3")
        self.write(arg=self.left_score, move=False, align="center", font=FONT)
        self.setx(100)
        self.write(arg=self.right_score, move=False, align="center", font=FONT)
        self.draw_line()

    def update_left_score(self):
        """Increment the left player's score"""
        self.left_score += 1
        self.clear()
        self.setx(-100)
        self.write(arg=self.left_score, move=False, align="center", font=FONT)
        self.setx(100)
        self.write(arg=self.right_score, move=False, align="center", font=FONT)
        self.draw_line()

    def update_right_score(self):
        """Increment the right player's score"""
        self.right_score += 1
        self.clear()
        self.setx(-100)
        self.write(arg=self.left_score, move=False, align="center", font=FONT)
        self.setx(100)
        self.write(arg=self.right_score, move=False, align="center", font=FONT)
        self.draw_line()

    def draw_line(self):
        """Draw a vertical line in the middle of the screen"""
        self.setx(0)
        for _ in range(6):
            self.write(arg="|", move=False, align="center", font=FONT)
            new_y = self.ycor() - 100
            self.sety(new_y)
        self.sety(220)
