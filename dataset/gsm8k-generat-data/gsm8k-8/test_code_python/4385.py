def solution():
    # Define the ratio of white scores to black scores
    white_black_ratio = 7/6

    # Total number of scores
    total_scores = 78

    # Total number of units in the ratio
    total_units = 7 + 6

    # Number of units of white scores
    white_units = total_scores / (white_black_ratio + 1)

    # Number of units of black scores
    black_units = total_scores - white_units

    # Difference between number of black and white scores
    diff = black_units - white_units

    # 2/3 of the difference
    result = (2/3) * diff
    return result

print(solution())