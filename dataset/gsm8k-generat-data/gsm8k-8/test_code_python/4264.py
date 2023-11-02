def solution():
    # Calculate the total points from Marcus' 3-point and 2-point goals
    points_from_3pointers = 5 * 3
    points_from_2pointers = 10 * 2
    total_points = points_from_3pointers + points_from_2pointers

    # Calculate the percentage of the team's total points that Marcus scored
    percentage_of_total_points = (total_points / 70) * 100
    result = percentage_of_total_points
    return result

print(solution())