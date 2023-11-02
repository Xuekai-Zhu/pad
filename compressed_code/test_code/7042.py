def solution():
    
    hornets_score = 86
    fireflies_score = 74
    three_pointer_score = 3
    two_pointer_score = 2
    fireflies_score += 7 * three_pointer_score
    hornets_score += 2 * two_pointer_score
    point_difference = fireflies_score - hornets_score
    result = point_difference
    return result

print(solution())