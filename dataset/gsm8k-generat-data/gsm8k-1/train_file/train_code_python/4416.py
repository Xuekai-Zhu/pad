def solution():
    """Levi and his brother were playing basketball. Levi had scored 8 times and his brother had scored 12 times. Levi was determined to beat his brother by at least 5 baskets. How many more times does Levi have to score in order to reach his goal if his brother scores another 3 times?"""
    levi_score = 8
    brother_score = 12
    brother_makes = 3
    goal_diff = 5
    score_diff = brother_score + brother_makes + goal_diff - levi_score
    result = score_diff
    return result

print(solution())