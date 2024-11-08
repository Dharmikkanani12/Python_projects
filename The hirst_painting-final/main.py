import random

# Define race settings
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = {color: 0 for color in colors}  # Track each turtle's position

# Get user's bet
user_bet = input("Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")

if user_bet in colors:
    is_race_on = True
else:
    print("Invalid color entered. Please restart and choose a valid color.")

# Simulate the race
while is_race_on:
    for color in all_turtles.keys():
        # Move each turtle a random amount
        rand_distance = random.randint(0, 10)
        all_turtles[color] += rand_distance

        # Check if any turtle has crossed the "finish line" (arbitrary 230 units)
        if all_turtles[color] >= 230:
            is_race_on = False
            winning_color = color
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break  # End the race if a winner is found
