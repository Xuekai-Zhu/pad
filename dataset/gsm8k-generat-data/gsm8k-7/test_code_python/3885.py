def solution():
    field_goal_points = 3
    num_field_goals = 13

    two_point_shots = 20
    two_point_points = 2

    # Calculate the total points from field goals
    field_goal_total = field_goal_points * num_field_goals

    # Calculate the total points from two point shots
    two_point_total = two_point_points * two_point_shots

    # Calculate the total points scored
    total_points = field_goal_total + two_point_total
    result = total_points
    return result

print(solution())