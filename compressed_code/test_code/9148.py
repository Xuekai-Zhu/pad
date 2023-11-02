def solution():
    
    three_point_goal_score = 5 * 3
    two_point_goal_score = 10 * 2
    total_score = three_point_goal_score + two_point_goal_score
    percent_of_total_score = (total_score / 70) * 100
    result = percent_of_total_score
    return result

print(solution())