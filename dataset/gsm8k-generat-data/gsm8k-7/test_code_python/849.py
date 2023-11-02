def solution():
    total_balloons = 200
    balloons_blowed_up_1 = total_balloons * (1/5)
    balloons_blowed_up_2 = 2 * balloons_blowed_up_1
    remaining_balloons = total_balloons - balloons_blowed_up_1 - balloons_blowed_up_2
    result = remaining_balloons
    return result

print(solution())