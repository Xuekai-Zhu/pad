def solution():
    levi_score = 8
    brother_score = 12
    brother_score += 3  # assuming the brother scores another 3 times
    target_score = brother_score + 5  # Levi needs to beat his brother by at least 5 baskets
    score_difference = target_score - levi_score  # calculate the difference in scores
    result = score_difference
    return result

print(solution())