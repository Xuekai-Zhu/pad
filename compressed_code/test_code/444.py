def solution():
    
    red_marbles = 20
    green_marbles = 3 * red_marbles
    yellow_marbles = 0.2 * green_marbles
    total_marbles = 3 * green_marbles
    blue_marbles = total_marbles - (red_marbles + green_marbles + yellow_marbles)
    result = blue_marbles
    return result

print(solution())