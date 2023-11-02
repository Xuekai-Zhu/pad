def solution():
    """Rachel solved 5 math problems each minute for 12 minutes before bed, but she didn't finish all of them. The next day, she finished the last 16 problems at lunch. How many math problems did she do in all?"""
    # Define the rate of problem solving and the time spent before bed
    rate = 5
    time_before_bed = 12

    # Calculate the number of problems solved before bed
    problems_solved_before_bed = rate * time_before_bed

    # Add the number of problems solved at lunchtime
    problems_solved_total = problems_solved_before_bed + 16

    result = problems_solved_total
    return result

print(solution())