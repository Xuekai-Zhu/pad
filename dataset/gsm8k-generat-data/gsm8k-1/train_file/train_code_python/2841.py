def solution():
    """Rachel solved 5 math problems each minute for 12 minutes before bed, but she didn't finish all of them.
    The next day, she finished the last 16 problems at lunch. How many math problems did she do in all?"""
    problems_per_minute = 5
    minutes_before_bed = 12
    problems_before_bed = problems_per_minute * minutes_before_bed
    total_problems = problems_before_bed + 16
    result = total_problems
    return result

print(solution())