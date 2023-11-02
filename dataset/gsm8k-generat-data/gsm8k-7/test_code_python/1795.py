def solution():
    jenny_red_marbles = 30
    jenny_blue_marbles = 25

    mary_red_marbles = jenny_red_marbles * 2
    anie_blue_marbles = jenny_blue_marbles * 2
    anie_red_marbles = mary_red_marbles + 20

    mary_blue_marbles = anie_blue_marbles / 2

    total_blue_marbles = jenny_blue_marbles + mary_blue_marbles + anie_blue_marbles
    result = total_blue_marbles
    return result

print(solution())