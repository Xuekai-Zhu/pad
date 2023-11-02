def solution():
    
    total_marbles = 63
    blue_marbles = total_marbles // 3
    green_marbles = 4
    red_marbles = total_marbles - blue_marbles - green_marbles
    result = red_marbles
    return result

print(solution())