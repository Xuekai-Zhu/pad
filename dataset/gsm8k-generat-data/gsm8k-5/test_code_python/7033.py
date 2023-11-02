def solution():
    total_hours = 9  # The night shift is 9 hours long
    first_guard_hours = 3  # The first guard takes 3 hours
    last_guard_hours = 2  # The last guard takes 2 hours
    middle_guard_hours = (total_hours - first_guard_hours - last_guard_hours) / 2  # The middle two guards split the remaining hours

    result = middle_guard_hours
    return result

print(solution())