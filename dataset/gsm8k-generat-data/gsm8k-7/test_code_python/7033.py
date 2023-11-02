def solution():
    night_shift_hours = 9
    first_guard_hours = 3
    last_guard_hours = 2

    # Calculate the total number of hours that the middle guards need to cover
    middle_guard_hours = night_shift_hours - first_guard_hours - last_guard_hours

    # Calculate the number of hours that each middle guard will take, since they are splitting the remaining time evenly
    hours_per_guard = middle_guard_hours / 2
    result = hours_per_guard
    return result

print(solution())