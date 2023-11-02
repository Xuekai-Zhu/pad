def solution():
    initial_leaves = 340
    daily_drop = initial_leaves / 10  # Determine the daily drop (1/10 of initial quantity)
    total_drop = daily_drop * 4  # Determine the total drop over four days
    fifth_day_drop = initial_leaves - total_drop  # Determine the drop on the fifth day
    result = fifth_day_drop
    return result

print(solution())