def solution():
    
    free_throw_points = 1
    three_point_points = 3
    jump_shot_points = 2
    liz_points = (5 * free_throw_points) + (3 * three_point_points) + (4 * jump_shot_points)
    opposing_team_points = 10
    final_score_difference = 20 - (liz_points - opposing_team_points)
    result = final_score_difference
    return result

print(solution())