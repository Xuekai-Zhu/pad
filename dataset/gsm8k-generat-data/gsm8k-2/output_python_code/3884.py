def solution():
    """James scored 13 field goals worth 3 points and 20 shots worth two points. How many total points did he score?"""
    field_goals = 13
    field_goal_points = 3
    field_goal_score = field_goals * field_goal_points
    shots = 20
    shot_points = 2
    shot_score = shots * shot_points
    total_score = field_goal_score + shot_score
    result = total_score
    return result

print(solution())