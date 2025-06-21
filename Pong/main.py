from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


LEFT_KEYS = ["w", "s"]
RIGHT_KEYS = ["Up", "Down"]

# Initialize the game window
screen = Screen()
screen.title("Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

# Initialize the paddles, ball and scoreboard
left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

# Listening for events and acting accordingly
screen.listen()
screen.onkeypress(key=LEFT_KEYS[0], fun=left_paddle.up)
screen.onkeypress(key=LEFT_KEYS[1], fun=left_paddle.down)
screen.onkeypress(key=RIGHT_KEYS[0], fun=right_paddle.up)
screen.onkeypress(key=RIGHT_KEYS[1], fun=right_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.006)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detecting collision with right paddle
    if abs(ball.ycor() - right_paddle.ycor()) <= 50:
        if right_paddle.xcor() - ball.xcor() <= 20:
            ball.paddle_bounce()

    # Detecting collision with right paddle
    if abs(ball.ycor() - left_paddle.ycor()) <= 50:
        if ball.xcor() - left_paddle.xcor() <= 20:
            ball.paddle_bounce()

    # Detecting if ball goes out of bounds
    if ball.xcor() - left_paddle.xcor() < -10:
        scoreboard.update_right_score()
        ball.reset()

    if ball.xcor() - right_paddle.xcor() > 10:
        scoreboard.update_left_score()
        ball.reset()

    ball.move()


screen.exitonclick()
