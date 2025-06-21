from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("JetBrainsMono", 15, "normal")
GAME_OVER_FONT = ("JetBrainsMono", 25, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("powderblue")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.show_score()


    def show_score(self):
        """Show the scoreboard."""
        self.clear()
        self.write(
            arg=f"Score: {self.score}   High score: {self.high_score}", move=False, align=ALIGNMENT, font=SCORE_FONT
        )

    def increase_score(self):
        """Show the scoreboard"""
        self.score += 1
        self.show_score()

    def game_over(self):
        """Display the game over message"""
        self.goto(0, 0)
        self.color("red")
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
