def solution():
    current_average = (80 + 75 + 90) / 3
    desired_average = 85
    last_test_weight = 4
    
    # Calculate the minimum score Carl needs on his last test to achieve the desired average
    min_last_test_score = (desired_average * (last_test_weight + 3)) - (80 + 75 + 90)
    result = min_last_test_score
    return result

print(solution())