def solution():
    total_balloons = 303 + 453
    balloons_shared = total_balloons / 2
    balloons_left = total_balloons - balloons_shared
    result = balloons_left
    return result

print(solution())