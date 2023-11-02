def solution():
    
    three_point_score = 3
    three_point_count = 15
    two_point_score = 2
    two_point_count = 12
    total_score = 75
    one_point_score = (total_score - (three_point_score * three_point_count) - (two_point_score * two_point_count))/1
    result = one_point_score
    return result

print(solution())