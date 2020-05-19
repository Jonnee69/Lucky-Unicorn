token = input("choose a token: ")

COST = 1

UNICORN = 5
ZEB_HOR = 0.5

balance = 10

# Adjust balance based on the chosen and generate feedback
if token == "unicorn":
    # prints unicorn statement
    print()
    print("*******************************************")
    print("***** Congratulations! It's ${:.2f} {} ****".format(UNICORN, token))
    print("*******************************************")

    balance+= UNICORN  # wins $5

elif token == "donkey":
    # prints donkey statement
    print()
    print("----------------------------------------------------------")
    print("| Sorry. It's a {}. You did win anything this round |".format(token))
    print("----------------------------------------------------------")

    balance -= COST   # does not win anything (ie: loses $1)

else:
    # prints donkey statement
    print()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("< Good try. It's a {}. You won back 50c >".format(token))

    balance -= ZEB_HOR # 'wins' 50c, paid $1 so loses 50c