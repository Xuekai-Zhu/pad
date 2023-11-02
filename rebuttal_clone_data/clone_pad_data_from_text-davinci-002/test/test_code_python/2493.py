def solution():
    yellow_scores = 78
    black_to_white_ratio = 7 / 6
    white_scores = yellow_scores / (black_to_white_ratio + 1)
    black_scores = white_scores * black_to_white_ratio
    difference = black_scores - white_scores
    two_thirds_difference = (2 / 3) * difference
    result = two_thirds_difference
    return result

print(solution())