
def prompt():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")


def direction():
    return  input("You're at a cross road. Where do you want to go? Type \"L\" or \"R\"\n").upper()


def action(count):
    if count == 0:
        return input("You have come to a lake. There is an island in the middle of the lake. "
                       "Type \"wait\" to wait for a boat. "
                       "Type \"swim\" to swim across.\n").lower()
    else:
        return input("Do you want to continue waiting (\"wait\") Or would you like to swim? (\"swim\")?\n").lower()


def color():
    return input("You arrive at the island unharmed. There is a house with 3 doors. "
                  "One red (R), one yellow (Y), and one blue (B). Which colour do you choose?\n").upper()


def game():
    """Winning path is: R -> wait -> wait -> swim -> Blue"""

    # MOVE 1
    if not direction().startswith("R"): lose()

    # MOVE 2
    if not action(0) == "wait": lose()

    # MOVE 3
    if not action(1) == "wait": lose()

    # MOVE 4
    if not action(2) == "swim": lose()

    # MOVE 5
    if not color() == "B": lose()


def win():
    print("You Win!")
    exit()


def lose():
    print("You Lose!")

    play_again = input("Would you like to play again?\n").upper()

    if play_again.startswith("Y"):
        game()
    else:
        exit()


if __name__ == "__main__":
    prompt()
    game()
