def solution():
    # Jenny's marbles
    jenny_red = 30
    jenny_blue = 25

    # Anie's marbles
    anie_red = jenny_red * 2 + 20
    anie_blue = jenny_blue * 2

    # Mary's marbles
    mary_red = jenny_red * 2
    mary_blue = anie_blue / 2

    # Total blue marbles collected
    total_blue = mary_blue + jenny_blue + anie_blue

    result = total_blue
    return result

print(solution())