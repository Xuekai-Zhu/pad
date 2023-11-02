def solution():
    last_week_jacks = 324  # Kenny did 324 jumping jacks last week
    this_week_jacks = [34, 20, 0, 123, 64, 23]  # Jumping jacks done by Kenny this week
    max_jacks = max(this_week_jacks)  # Find the maximum number of jumping jacks Kenny did this week

    # Calculate the minimum number of jumping jacks Kenny needs to do on Saturday to beat last week's record
    min_jacks_on_saturday = last_week_jacks - sum(this_week_jacks) + max_jacks + 1
    result = min_jacks_on_saturday
    return result

print(solution())