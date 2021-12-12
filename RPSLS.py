import random

list1 = ["Rock", "Spock", "Paper", "Lizard", "Scissors"]

print("Welcome to rock paper scissors lizard spock", "\n", "0 - Rock", "\n", "1 - Spock", "\n", "2 - Paper", "\n", "3 - Lizard", "\n", "4 - Scissors")

Choice = int(input("please make a decision on what to use"))

x = random.randint(1, 4)


if (Choice == 0):

    print("you chose Rock")

    print("computer choice " + list1[x])

    if (list1[x] == "Paper"):

        print("you lose")

    if (list1[x] == "Scissors"):
        print("you win")

    if (list1[x] == "Lizard"):
        print("you win")

    if (list1[x] == "Spock"):
        print("you lose")

    else:
        print("tie")


if (Choice == 1):

    print("you chose Spock")

    print("computer choice " + list1[x])

    if (list1[x] == "Paper"):
        print("you lose")

    if (list1[x] == "Scissors"):
        print("you win")

    if (list1[x] == "Rock"):
        print("you win")

    if (list1[x] == "Lizard"):
        print("you lose")

    if (list1[x] == "Paper"):
        print("you lose")

    else:
        print("tie")


if (Choice == 2):

    print("you chose Paper")

    print("computer choice " + list1[x])

    if (list1[x] == "Rock"):
        print("you win")

    if (list1[x] == "Scissors"):
        print("you lose")

    if (list1[x] == "Lizard"):
        print("you lose")

    if (list1[x] == "Spock"):
        print("you win")

    else:
        print("tie")


if (Choice == 3):

    print("you chose Paper")

    print("computer choice " + list1[x])

    if (list1[x] == "Spock"):
        print("Spock")

    if (list1[x] == "Paper"):
        print("you win")

    if (list1[x] == "Scissors"):
        print("you lose")

    if (list1[x] == "Rock"):
        print("you lose")

    else:
        print("tie")

if (Choice == 4):

    print("you chose Scissors")

    print("computer choice " + list1[x])

    if (list1[x] == "Spock"):
        print("you lose")

    if (list1[x] == "Paper"):
        print("you win")

    if (list1[x] == "Lizard"):
        print("you win")

    if (list1[x] == "Rock"):
        print("you lose")

    else:
        print("tie")
