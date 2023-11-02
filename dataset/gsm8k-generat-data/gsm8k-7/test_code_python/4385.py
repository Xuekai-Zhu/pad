def solution():
    yellow_scores = 78
    white_to_black_ratio = 7/6

    # Calculate the total number of parts in the ratio
    total_parts = 7 + 6

    # Calculate the number of parts that represent white scores
    white_parts = total_parts / (1 + white_to_black_ratio)

    # Calculate the number of parts that represent black scores
    black_parts = white_to_black_ratio * white_parts

    # Calculate the number of white scores used
    num_white_scores = (white_parts / total_parts) * yellow_scores

    # Calculate the number of black scores used
    num_black_scores = (black_parts / total_parts) * yellow_scores

    # Calculate the difference between the number of black and white scores used
    diff_scores = abs(num_black_scores - num_white_scores)

    # Calculate 2/3 of the difference between black and white scores
    result = (2/3) * diff_scores
    return result

print(solution())