def solution():
    
    yellow_ratio = 7 + 6
    yellow_scores = 78
    white_scores = (6 / yellow_ratio) * yellow_scores
    black_scores = (7 / yellow_ratio) * yellow_scores
    difference = abs(black_scores - white_scores)
    two_thirds_difference = (2 / 3) * difference
    result = two_thirds_difference
    return result

print(solution())