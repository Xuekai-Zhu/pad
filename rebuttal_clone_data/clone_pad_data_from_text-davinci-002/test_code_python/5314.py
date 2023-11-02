def solution():
    total_balls = 15 + 5
    balls_removed = 8 * 3
    remaining_balls = total_balls - balls_removed
    result = remaining_balls / 2
    return result

print(solution())