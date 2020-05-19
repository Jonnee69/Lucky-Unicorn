# Function to easily generate winnings....

def token_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print


# Main routine

COST = 1    # cost per round
UNICORN = 5     # unicorn wins $5
ZEB_HOR = 0.5   # zebra / horse "wins" 50c
DONKEY = 0      # donkey does not win anything

tokens = ["unicorn", "horse", "donkey", "zebra"]

for token in tokens:

    if token == "unicorn":
        token_statement("*****   Congratulations! It's a ${:.2f} {} *******".format(UNICORN, token), "*")
    elif token == "donkey":
        token_statement("-- Sorry.  It's a {}. You did not win anything this round --".format(token), "-")
    else:
        token_statement("^^ Good try. It's a {}. You won back 50c ^^".format(token), "^")
