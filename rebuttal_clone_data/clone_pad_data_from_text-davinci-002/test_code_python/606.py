def solution():
    red_marbles = 20
    green_marbles = red_marbles * 3
    yellow_marbles = green_marbles * 0.2
    total_marbles = green_marbles + red_marbles + yellow_marbles
    different_color_marbles = total_marbles - green_marbles
    result = different_color_marbles
    return result

print(solution())