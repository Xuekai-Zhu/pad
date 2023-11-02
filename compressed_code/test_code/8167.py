def solution():
    
    total_marbles = 50
    white_marbles = total_marbles / 2
    yellow_marbles = 12
    green_marbles = yellow_marbles / 2
    red_marbles = total_marbles - (white_marbles + yellow_marbles + green_marbles)
    result = red_marbles
    return result

print(solution())