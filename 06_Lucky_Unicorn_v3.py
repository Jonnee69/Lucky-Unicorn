# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability




# v3 - put 'token statements into if statements
#   change the format of each statement so that unicorn is visually different to
#   and donkey
# v4 Added rounds counter
# v5 Made program flexible
# v6 Made token statement automatically (also improved flexbility)

import random

# Integer checking function below
def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)


# function to print out out 'token statements'. Takes in message and then applies 'decoration'
# and bottom of message based on specified character
def token_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()


# Main routine

# Cost Payout Constants
COST = 1    # cost per round
UNICORN = 5     # unicorn wins $5
ZEB_HOR = 0.5   # zebra / horse "wins" 50c
DONKEY = 0      # donkey does not win anything

# Introduction / Instructions

print("**** Welcome to the Lucky Unicorn Game ****")
print()
print("To play, enter an amount of money between $1 and $10 (whole dollars only).")
print()
print("- It costs $1/round")
print()
print("Payouts")




# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with? $", 1, 10)
round_count = 0

print("***** Game in Progress ******")

keep_going = ""
while keep_going == "":

    # tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    round_count +=1

    # Adjust balance based on the chosen and generate feedback
    if token == "unicorn":
        # create and print unicorn statement

        token_statement("*****   Congratulations! It's a ${:.2f} {} *******".format(UNICORN, token), "*")
        balance += UNICORN    # wins $5

    elif token == "donkey":
            # prints donkey statement
        token_statement("-- Sorry.  It's a {}. You did not win anything this round --".format(token), "-")
        balance -= COST    # does not win anything (ie: loses $1)

    else:
        # prints zebra / horse statement
        token_statement("^^ Good try. It's a {}. You won back 50c ^^".format(token), "-")
        balance -= ZEB_HOR  # 'wins' 50c, paid $1 so losses 50c

    print()
    print("Rounds Played: {}         Balance: ${:.2f}".format(round_count, balance))
    print()

    # If user has enough money to play, ask if they want to play again...
    if balance < COST:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any to quit")