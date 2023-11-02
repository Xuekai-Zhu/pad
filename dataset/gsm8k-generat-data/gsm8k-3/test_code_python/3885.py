def solution():
    """James scored 13 field goals worth 3 points and 20 shots worth two points.  How many total points did he score?"""
    # Define the number of field goals and their point value
    field_goals = 13
    field_goal_points = 3

    # Define the number of two-point shots and their point value
    two_point_shots = 20
    two_point_points = 2

    # Calculate the total points scored
    total_points = (field_goals * field_goal_points) + (two_point_shots * two_point_points)

    # Display the total points
    result = total_points
    return result

print(solution())