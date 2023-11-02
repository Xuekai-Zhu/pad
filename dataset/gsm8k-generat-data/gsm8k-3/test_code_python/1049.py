def solution():
    """In a math test, Mark scored twice as much as the least score. If the highest score is 98 and the range of the scores is 75, what was Mark's score?"""
    # Define the highest score and the range
    highest_score = 98
    score_range = 75

    # Calculate the least score
    least_score = highest_score - score_range

    # Calculate Mark's score
    mark_score = 2 * least_score

    # Display Mark's score
    result = mark_score
    return result

print(solution())