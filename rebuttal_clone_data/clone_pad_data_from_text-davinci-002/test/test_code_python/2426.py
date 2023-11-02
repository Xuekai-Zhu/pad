def solution():
    total_points = 70
    three_point_goals = 5
    two_point_goals = 10

    three_point_value = 3
    two_point_value = 2

    total_points_scored = (three_point_goals * three_point_value) + (two_point_goals * two_point_value)
    percent_scored = (total_points_scored / total_points) * 100
    result = percent_scored
    return result

print(solution())