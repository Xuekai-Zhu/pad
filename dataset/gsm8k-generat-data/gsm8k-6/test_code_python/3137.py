def solution():
    # Calculate the total score of the students who scored a 92 and the students who scored an 80
    total_score = 5 * 92 + 4 * 80

    # Calculate the minimum total score needed for the class average to be at least 85
    min_total_score = 85 * 10

    # Calculate the score the last student needs to achieve to meet the class average requirement
    score_needed = min_total_score - total_score

    result = score_needed
    return result

print(solution())