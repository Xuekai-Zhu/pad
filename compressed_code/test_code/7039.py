def solution():
    
    yellow_balloons = 3414
    black_balloons = yellow_balloons + 1762
    total_balloons = yellow_balloons + black_balloons
    balloons_per_school = total_balloons / 10
    result = balloons_per_school
    return result

print(solution())