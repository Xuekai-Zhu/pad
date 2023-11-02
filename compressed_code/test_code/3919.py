def solution():
    
    total_problems = 20
    martha_problems = 2
    jenna_problems = (4 * martha_problems) - 2
    mark_problems = jenna_problems / 2
    angela_problems = total_problems - (martha_problems + jenna_problems + mark_problems)
    result = angela_problems
    return result

print(solution())