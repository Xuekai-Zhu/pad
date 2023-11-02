def solution():
    
    total_marbles = 19
    yellow_marbles = 5
    remaining_marbles = total_marbles - yellow_marbles
    blue_marbles = remaining_marbles * 3 / 7
    red_marbles = remaining_marbles * 4 / 7
    difference = red_marbles - yellow_marbles
    result = difference
    return result

print(solution())