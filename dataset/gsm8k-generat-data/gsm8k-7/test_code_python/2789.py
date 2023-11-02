def solution():
    # Find the sum of Maria's first three test scores
    total_score = 80 + 70 + 90
    
    # Compute the score needed to achieve an average of 85 across all four tests
    desired_avg = 85
    num_tests = 4
    needed_score = (desired_avg * num_tests) - total_score
    
    result = needed_score
    return result

print(solution())