def solution():
    # Calculate last week's total
    last_week_total = 324

    # Calculate this week's total
    this_week_total = 34 + 20 + 0 + 123 + 64 + 23

    # Calculate the difference between this week's total and last week's total
    difference = this_week_total - last_week_total

    # Calculate the minimum number of jumping jacks Kenny needs to do on Saturday to beat last week's total
    min_jumping_jacks = last_week_total + difference + 1

    result = min_jumping_jacks
    return result

print(solution())