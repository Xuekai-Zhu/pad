def solution():
    initial_supplies = 400  # The ship initially had 400 pounds of food
    first_day_usage = (2/5) * initial_supplies  # 2/5 of the supplies were used on the first day
    supplies_after_first_day = initial_supplies - first_day_usage  # Remaining supplies after the first day
    second_day_usage = (3/5) * supplies_after_first_day  # 3/5 of the remaining supplies were used on the second and third day
    supplies_remaining = supplies_after_first_day - second_day_usage  # Supplies remaining after the second and third day
    result = supplies_remaining
    return result

print(solution())