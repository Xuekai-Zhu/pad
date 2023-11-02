def solution():
    test_scores = [85, 79, 92, 84]
    current_avg = sum(test_scores) / len(test_scores)
    desired_avg = 85

    # Calculate the score needed on the fifth test to reach the desired average
    needed_score = (desired_avg * (len(test_scores) + 1)) - sum(test_scores)
    result = needed_score
    return result

print(solution())