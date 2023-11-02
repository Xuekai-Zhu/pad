def solution():
    
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