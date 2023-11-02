def solution():
    """In a math test, Mark scored twice as much as the least score. If the highest score is 98 and the range of the scores is 75, what was Mark's score?"""
    highest_score = 98
    range_of_scores = 75
    least_score = highest_score - range_of_scores
    mark_score = least_score * 2
    result = mark_score
    return result

print(solution())