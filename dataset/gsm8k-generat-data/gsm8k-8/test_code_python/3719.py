def solution():
    total_problems = 75
    time1 = 20
    problems1 = 10
    time2 = 40
    problems2 = (total_problems - problems1) * 0.5
    
    # Calculate how many problems she has left to solve
    remaining_time = time1 + time2
    remaining_problems = total_problems - problems1 - problems2
    remaining_problems_per_minute = remaining_problems / remaining_time
    problems_left = remaining_problems_per_minute * 40
    result = problems_left
    return result

print(solution())