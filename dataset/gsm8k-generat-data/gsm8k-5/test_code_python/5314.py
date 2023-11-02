def solution():
    # Total number of balls in all baskets before any balls are removed
    total_balls = 15 * 5 + 5 * 5

    # Total number of balls removed by the first 3 students
    balls_removed = 8 * 3

    # Total number of balls remaining
    balls_remaining = total_balls - balls_removed - 56

    # Number of balls removed by the other 2 students combined
    balls_removed_other = balls_remaining / 2

    # Number of balls removed by each of the other 2 students
    balls_each = balls_removed_other / 2

    result = balls_each
    return result

print(solution())