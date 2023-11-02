def solution():
    
    total_marbles = 60
    yellow_marbles = 20
    green_marbles = yellow_marbles / 2
    red_blue_marbles = total_marbles - yellow_marbles - green_marbles
    blue_marbles = red_blue_marbles / 2
    probability_blue = (blue_marbles / total_marbles) * 100
    result = probability_blue
    
    return result

print(solution())