def solution():
    
    total_balloons = 672
    groups = 4 
    balloons_per_group = total_balloons / groups
    yellow_balloons = balloons_per_group 
    balloons_taken = yellow_balloons / 2
    result = balloons_taken
    return result

print(solution())