def solution():
    
    sammy_score = 20
    gab_score = 2 * sammy_score
    cher_score = 2 * gab_score
    total_score = sammy_score + gab_score + cher_score
    opponent_score = 85
    points_above_opponent = total_score - opponent_score
    result = points_above_opponent
    return result

print(solution())