def solution():
    
    current_total = 80 + 70 + 90
    current_num_tests = 3
    desired_average = 85
    num_tests_needed = 4
    score_needed = (desired_average * num_tests_needed) - current_total
    return score_needed

print(solution())