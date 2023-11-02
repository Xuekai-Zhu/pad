def solution():
    total_shift_hours = 9
    first_guard_hours = 3
    last_guard_hours = 2

    # Calculate the total hours remaining for the middle two guards
    remaining_hours = total_shift_hours - first_guard_hours - last_guard_hours

    # Divide the remaining hours equally between the middle two guards
    middle_guards_hours = remaining_hours / 2
    result = middle_guards_hours
    return result

print(solution())