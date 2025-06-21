from turtle import Turtle, Screen
import pandas

HEIGHT = 491
WIDTH = 725
FONT = ("JetBrainsMono", 7, "bold")

# Initializing the game window
screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.title("US States Game")
image = "blank_states.gif"
screen.bgpic(image)

# Reading the csv file
data = pandas.read_csv("50_states.csv")
num_states = len(data)
state_names = data.state.to_list()

# Initializing a turtle to write the names
turtle = Turtle()
turtle.penup()
turtle.color("black")
turtle.hideturtle()

# The main game loop
correct_guesses = 0
game_is_on = True
guessed_states = []
while game_is_on:
    user_answer = screen.textinput(
        title=f"{correct_guesses}/{num_states} guessed",
        prompt="Name a state",
    ).title()
    if user_answer == "Exit":
        unguessed_states = []
        for state in state_names:
            if state not in guessed_states:
                unguessed_states.append(state)
        unguessed_state_data = pandas.DataFrame(unguessed_states)
        unguessed_state_data.to_csv("unguessed_states.csv")
        break
    if user_answer in state_names and user_answer not in guessed_states:
        correct_guesses += 1
        guessed_states.append(user_answer)
        guessed_state = data[data.state == user_answer]
        turtle.goto(guessed_state.x.item(), guessed_state.y.item())
        turtle.write(arg=user_answer, move=False, align="center", font=FONT)
    if correct_guesses == num_states:
        game_is_on = False


screen.exitonclick()
