from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

KEYS = ["w", "a", "s", "d"]
# KEYS = ["Up", "Left", "Down", "Right"]

# Initializing the game window
screen = Screen()
screen.title("Snake")
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.tracer(0)

# Initialize the snake, the food and the scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keypresses
screen.listen()
screen.onkey(snake.up, KEYS[0])
screen.onkey(snake.left, KEYS[1])
screen.onkey(snake.down, KEYS[2])
screen.onkey(snake.right, KEYS[3])

# Begin the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
