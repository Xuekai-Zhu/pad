def solution():
    total_marbles = 19
    yellow_marbles = 5
    blue_marbles = (total_marbles - yellow_marbles) / 3
    red_marbles = total_marbles - yellow_marbles - blue_marbles
    result = red_marbles - yellow_marbles
    return result

print(solution())