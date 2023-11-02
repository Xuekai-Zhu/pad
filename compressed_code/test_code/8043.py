def solution():
    
    problems_per_minute = 5
    minutes_before_bed = 12
    problems_before_bed = problems_per_minute * minutes_before_bed
    total_problems = problems_before_bed + 16
    result = total_problems
    return result

print(solution())