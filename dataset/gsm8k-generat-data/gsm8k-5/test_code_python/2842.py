def solution():
    math_problems_per_minute = 5  # Rachel solved 5 math problems each minute
    time_before_bed = 12  # Rachel worked for 12 minutes before bed
    problems_before_bed = math_problems_per_minute * time_before_bed  # Calculate the number of problems she solved before bed

    # Calculate the total number of math problems Rachel did
    total_math_problems = problems_before_bed + 16  # She finished the remaining 16 problems at lunch

    result = total_math_problems
    return result

print(solution())