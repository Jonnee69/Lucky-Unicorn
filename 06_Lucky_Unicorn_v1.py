# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random

# Integer checking function below
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! Please enter an integer between {} and {}".format(low, high)
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)

# Main routine

# Ask user how much they want to play with? (min $1, max $10)
balance = intcheck("How much money would you like to play with? $", 1, 10)

keep_going = ""
while keep_going == "":

    # tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    # Adjust balance based on the chosen and generate feedback
    if token == "unicorn":
        balance += 5   # wins $5
        feedback = "Congratulations you won $5.00"
    elif token == "donkey":
        balance -= 1    # does not win anything (ie: loses $1)
        feedback = "Sorry, you did not win anything this round"
    else:
        balance -= 0.5  # 'wins' 50c, paid $1 so loses 50c
        feedback = "Congratulations you won 50c"

    print()
    print(feedback)
    print("You have ${} to play with".format(balance))
    print()

    # If user has enough money to play, ask if they want to play again...
    if balance < 1:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any to quit")

# farewell user at end of game.
print("Thank you for playing.")