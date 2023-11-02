def solution():
    
    balloons_per_dozen = 12
    initial_balloons = 3 * balloons_per_dozen
    balloons_bought = 3 + 12
    balloons_left = initial_balloons - balloons_bought
    result = balloons_left
    return result

print(solution())