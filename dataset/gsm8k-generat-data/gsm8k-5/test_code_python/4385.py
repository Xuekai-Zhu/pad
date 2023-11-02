def solution():
    # Calculate the total ratio between white and black scores
    total_ratio = 7 + 6

    # Calculate the fraction of the ratio that represents white scores
    white_score_ratio = 7 / total_ratio

    # Calculate the fraction of the ratio that represents black scores
    black_score_ratio = 6 / total_ratio

    # Calculate the total number of yellow scores
    total_yellow_scores = 78

    # Calculate the number of white scores used
    white_scores = total_yellow_scores * white_score_ratio

    # Calculate the number of black scores used
    black_scores = total_yellow_scores * black_score_ratio

    # Calculate the difference between the number of black and white scores
    score_difference = black_scores - white_scores

    # Calculate 2/3 of the score difference
    two_thirds_difference = (2/3) * score_difference

    result = two_thirds_difference
    return result

print(solution())