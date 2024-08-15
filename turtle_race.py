from turtle import Turtle, Screen
import random
import pygame

# Initialize Pygame for sound effects
pygame.mixer.init()

# Load the sound files
start_sound = pygame.mixer.Sound('sound/start.wav')
win_sound = pygame.mixer.Sound('sound/win.wav')
lose_sound = pygame.mixer.Sound('sound/lose.wav')

# Setup the screen
screen = Screen()
screen.setup(width=600, height=400)  # Increased width for button space
screen.title("Turtle Race")

# Initialize the scoreboard
wins = 0
losses = 0

# Create a turtle for displaying the scoreboard
score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-200, 150)
score_turtle.color("black")

# Create a turtle for the restart button
button_turtle = Turtle()
button_turtle.penup()
button_turtle.goto(200, 150)
button_turtle.shape("square")
button_turtle.shapesize(stretch_wid=2, stretch_len=4)
button_turtle.color("lightblue")
button_turtle.write("Restart", align="center", font=("Arial", 12, "bold"))
button_turtle.hideturtle()

# List to keep track of active turtles
all_turtles = []

def update_scoreboard():
    score_turtle.clear()
    score_turtle.write(f"Wins: {wins}  Losses: {losses}", align="left", font=("Arial", 16, "normal"))

def play_sound(sound):
    pygame.mixer.Sound.play(sound)

def setup_turtles():
    global all_turtles
    # Clear existing turtles
    for turtle in all_turtles:
        turtle.hideturtle()
        turtle.clear()
    all_turtles = []  # Reset the list of turtles

    colors = ["red", "blue", "green", "purple", "orange", "yellow"]
    y_positions = [-70, -40, -10, 20, 50, 80]

    for turtle_index in range(0, 6):
        tim = Turtle(shape="turtle")
        tim.color(colors[turtle_index])
        tim.penup()
        tim.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(tim)

def start_race():
    global wins, losses
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color:")

    setup_turtles()

    if user_bet:
        play_sound(start_sound)
        is_race_on = True

        while is_race_on:
            for turtle in all_turtles:
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        print(f"You won! The {winning_color} turtle is the winner!")
                        play_sound(win_sound)
                        wins += 1
                    else:
                        print(f"You lost! The {winning_color} turtle is the winner!")
                        play_sound(lose_sound)
                        losses += 1

                    # Update the scoreboard on the screen
                    update_scoreboard()

                    # Clear the turtles for the next race
                    for t in all_turtles:
                        t.hideturtle()
                    return  # Exit the function to avoid additional races

                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)

def check_click(x, y):
    # Check if the restart button was clicked
    if 170 < x < 230 and 130 < y < 170:
        start_race()

# Bind the click event to the check_click function
screen.onscreenclick(check_click)

# Show the initial scoreboard
update_scoreboard()

# Run the first race
start_race()

# Keep the screen open until the user closes it
screen.mainloop()
