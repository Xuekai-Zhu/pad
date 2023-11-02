def solution():
    yellow_marbles = 20
    green_marbles = yellow_marbles / 2
    red_marbles = (60 - yellow_marbles - green_marbles) / 2
    blue_marbles = red_marbles
    total_marbles = yellow_marbles + green_marbles + red_marbles + blue_marbles
    probability_blue = blue_marbles / total_marbles
    result = probability_blue * 100
    return result

print(solution())