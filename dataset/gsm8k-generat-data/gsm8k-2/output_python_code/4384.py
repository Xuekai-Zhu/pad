def solution():
    """To make a yellow score mixture, Taylor has to combine white and black scores in the ratio of 7:6. If she got 78 yellow scores, what's 2/3 of the difference between the number of black and white scores she used?"""
    yellow_ratio = 7 + 6
    yellow_scores = 78
    white_scores = (yellow_scores / yellow_ratio) * 7
    black_scores = (yellow_scores / yellow_ratio) * 6
    difference = abs(black_scores - white_scores)
    two_thirds_difference = (2 / 3) * difference
    result = two_thirds_difference
    return result

print(solution())