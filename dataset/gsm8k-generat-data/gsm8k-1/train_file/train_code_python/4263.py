def solution():
    """Marcus scored 5 3-point goals and 10 2-point goals. If his team scored 70 points overall, what percentage of the team's total points did Marcus score?"""
    three_point_goal_score = 5 * 3
    two_point_goal_score = 10 * 2
    total_score = three_point_goal_score + two_point_goal_score
    percent_of_total_score = (total_score / 70) * 100
    result = percent_of_total_score
    return result

print(solution())