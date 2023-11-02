def solution():
    """James scored 13 field goals worth 3 points and 20 shots worth two points. How many total points did he score?"""
    # Calculate the total points from field goals
    field_goal_points = 13 * 3

    # Calculate the total points from two-point shots
    two_point_points = 20 * 2

    # Calculate the total points
    total_points = field_goal_points + two_point_points

    # return the result
    result = total_points
    return result

print(solution())