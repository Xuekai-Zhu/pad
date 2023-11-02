def solution():
    total_marbles = 63
    red_marbles = 38
    green_marbles = red_marbles / 2
    dark_blue_marbles = total_marbles - red_marbles - green_marbles
    result = dark_blue_marbles
    
    return result

print(solution())