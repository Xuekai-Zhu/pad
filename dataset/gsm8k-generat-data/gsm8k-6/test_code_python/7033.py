def solution():
    # Calculate the total number of middle hours to be split by two guards
    total_middle_hours = 9 - 3 - 2  # first guard takes 3 hours, last guard takes 2 hours
    hours_per_guard = total_middle_hours / 2  # split the middle hours between 2 guards
    result = hours_per_guard
    return result

print(solution())