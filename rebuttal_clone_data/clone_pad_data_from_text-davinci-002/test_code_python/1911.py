def solution():
    balloons_added = 8
    balloons_popped = (12 + balloons_added) / 2
    total_balloons = (12 + balloons_added) - balloons_popped
    result = total_balloons
    return result

print(solution())