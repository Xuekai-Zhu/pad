def solution():
    # Calculate the total ratio of scores needed to make 78 yellow scores
    total_ratio = 7 + 6  # total ratio of white and black scores

    # Calculate the number of black scores used
    black_scores = (6/total_ratio) * 78  

    # Calculate the number of white scores used
    white_scores = (7/total_ratio) * 78  

    # Calculate the difference between the number of black and white scores used
    difference = abs(black_scores - white_scores)

    # Calculate 2/3 of the difference
    two_thirds_diff = (2/3) * difference
    result = two_thirds_diff
    return result

print(solution())