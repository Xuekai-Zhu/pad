def solution():
    """
    Mary collected twice as many red marbles as Jenny and half the number of blue marbles collected by Anie,
    who collected 20 more red marbles than Mary and twice the number of blue marbles Jenny collected.
    From Monday to Friday, Jenny collected 30 red marbles and 25 blue marbles.
    What's the total number of blue marbles collected by the friends together?
    """
    # Initialize variables
    mary_red = 0
    jenny_red = 30
    anie_red = 0
    jenny_blue = 25
    anie_blue = 2 * jenny_blue
    mary_blue = anie_blue / 2
    total_blue = jenny_blue + mary_blue + anie_blue

    return total_blue

print(solution())