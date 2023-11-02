def solution():
    """In a math test, Mark scored twice as much as the least score. If the highest score is 98 and the range of the scores is 75, what was Mark's score?"""
    # Define the highest and lowest scores
    highest_score = 98
    lowest_score = highest_score - 75

    # Calculate Mark's score
    mark_score = lowest_score * 2

    # return the result
    result = mark_score
    return result

print(solution())