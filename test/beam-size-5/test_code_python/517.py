def solution():
    
    total_problems = 100
    monday_problems = 12
    tuesday_problems = monday_problems * 3
    remaining_problems = total_problems - monday_problems - tuesday_problems
    wednesday_problems = remaining_problems / 4
    remaining_problems -= wednesday_problems
    result = remaining_problems
    return result

print(solution())