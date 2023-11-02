def solution():
    levi_score = 8
    brother_score = 12
    required_margin = 5
    brother_additional_score = 3

    # Calculate the minimum score Levi needs to beat his brother by 5 baskets
    required_levi_score = brother_score + required_margin + brother_additional_score

    # Calculate the difference between Levi's current score and the required score
    score_difference = required_levi_score - levi_score

    result = score_difference
    return result

print(solution())