def solution():
    # Calculate the total score of the 9 students who have already taken the test
    total_score = (5 * 92) + (4 * 80)

    # Calculate the score the 10th student would need to achieve an average of 85
    required_score = (85 * 10) - total_score

    result = required_score
    return result

print(solution())