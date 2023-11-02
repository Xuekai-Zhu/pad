def solution():
    
    total_marbles = 85
    red_marbles = 14
    blue_marbles = 3 * red_marbles
    yellow_marbles = total_marbles - red_marbles - blue_marbles
    result = yellow_marbles
    return result

print(solution())