def solution():
    # Jenny collected 30 red marbles
    jenny_red = 30
    jenny_blue = 25

    # Anie collected twice as many blue marbles as Jenny
    anie_blue = 2 * jenny_blue

    # Mary collected half the number of blue marbles collected by Anie
    mary_blue = anie_blue / 2

    # Anie collected 20 more red marbles than Mary
    anie_red = 2 * mary_red + 20

    # Mary collected twice as many red marbles as Jenny
    mary_red = 2 * jenny_red

    # Total number of blue marbles collected
    total_blue = jenny_blue + mary_blue + anie_blue
    result = total_blue
    return result

print(solution())