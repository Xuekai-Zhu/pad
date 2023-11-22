def solution():
    
    total_problems = 100
    monday_problems = 12
    tuesday_problems = 3 * monday_problems
    remaining_problems = total_problems - monday_problems - tuesday_problems
    wednesday_problems = remaining_problems / 4
    problems_left = remaining_problems - wednesday_problems
    result = problems_left
    return result

print(solution())