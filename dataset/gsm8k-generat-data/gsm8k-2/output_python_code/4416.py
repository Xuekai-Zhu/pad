def solution():
    """Levi and his brother were playing basketball. Levi had scored 8 times and his brother had scored 12 times. Levi was determined to beat his brother by at least 5 baskets. How many more times does Levi have to score in order to reach his goal if his brother scores another 3 times?"""
    levi_score = 8
    brother_score = 12 + 3
    goal_diff = 5
    score_diff = brother_score - levi_score
    if score_diff < goal_diff:
        levi_more_score = goal_diff - score_diff
    else:
        levi_more_score = 0
    result = levi_more_score
    return result

print(solution())