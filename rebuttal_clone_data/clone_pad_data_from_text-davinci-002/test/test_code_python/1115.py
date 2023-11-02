def solution():
    round_balloons = 5 * 20
    long_balloons = 4 * 30
    total_balloons = round_balloons + long_balloons
    balloons_that_burst = 5
    balloons_left = total_balloons - balloons_that_burst
    result = balloons_left
    return result

print(solution())