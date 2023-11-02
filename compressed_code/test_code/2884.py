def solution():
    
    total_problems = 75
    first_completion_time = 20
    first_completion_problems = 10
    second_completion_time = 40
    second_completion_problems = 2 * first_completion_problems
    remaining_completion_time = 40
    remaining_problems = total_problems - first_completion_problems - second_completion_problems
    result = remaining_problems
    return result

print(solution())