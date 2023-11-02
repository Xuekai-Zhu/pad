def solution():
    """To make a yellow score mixture, Taylor has to combine white and black scores in the ratio of 7:6. If she got 78 yellow scores, what's 2/3 of the difference between the number of black and white scores she used?"""
    # Define the ratio of white to black scores
    WHITE_TO_BLACK_RATIO = 7 / 6

    # Calculate the total number of scores used to make the yellow score mixture
    total_scores = 78 / (1 + WHITE_TO_BLACK_RATIO)

    # Calculate the number of white and black scores used
    white_scores = total_scores * WHITE_TO_BLACK_RATIO
    black_scores = total_scores - white_scores

    # Calculate 2/3 of the difference between the number of black and white scores used
    diff = abs(black_scores - white_scores)
    result = (2 / 3) * diff
    return result

print(solution())