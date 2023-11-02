def solution():
    """James scored 13 field goals worth 3 points and 20 shots worth two points. How many total points did he score?"""
    field_goals = 13
    points_per_field_goal = 3
    shots = 20
    points_per_shot = 2
    total_points = field_goals * points_per_field_goal + shots * points_per_shot
    result = total_points
    return result

print(solution())