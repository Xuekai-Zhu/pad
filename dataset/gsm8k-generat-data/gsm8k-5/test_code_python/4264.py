def solution():
    points_from_3pointers = 5 * 3  # Marcus scored 5 3-point goals
    points_from_2pointers = 10 * 2  # Marcus scored 10 2-point goals

    # Total points scored by Marcus
    total_points = points_from_3pointers + points_from_2pointers

    # Percentage of team's total points scored by Marcus
    percentage_scored = (total_points / 70) * 100

    result = percentage_scored
    return result

print(solution())