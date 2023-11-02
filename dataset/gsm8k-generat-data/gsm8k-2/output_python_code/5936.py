def solution():
    """Beth has 72 marbles of three colors. Each color has the same amount of marbles. If Beth loses 5 red, twice as many blue, and three times as many yellow ones than red ones, how many marbles does she have left?"""
    total_marbles = 72
    red_marbles = total_marbles / 3
    blue_marbles = total_marbles / 3
    yellow_marbles = total_marbles / 3

    red_marbles -= 5
    blue_marbles -= 2 * 5
    yellow_marbles -= 3 * 5

    remaining_marbles = red_marbles + blue_marbles + yellow_marbles
    result = remaining_marbles
    return result

print(solution())