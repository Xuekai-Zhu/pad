def solution():
    
    num_problems = 20
    time_with_calculator = num_problems * 2
    time_without_calculator = num_problems * 5
    time_saved = time_without_calculator - time_with_calculator
    result = time_saved
    return result

print(solution())