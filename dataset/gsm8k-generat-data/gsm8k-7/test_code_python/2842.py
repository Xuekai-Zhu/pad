def solution():
    problems_per_minute = 5
    minutes_before_bed = 12
    problems_unfinished = problems_per_minute * minutes_before_bed

    total_problems = problems_unfinished + 16
    result = total_problems
    return result

print(solution())