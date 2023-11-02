def solution():
    # Calculate the sum of the scores so far
    sum_scores = (5 * 92) + (4 * 80)

    # Calculate the minimum score needed for an average of 85
    min_score = (85 * 10) - sum_scores
    result = min_score
    return result

print(solution())