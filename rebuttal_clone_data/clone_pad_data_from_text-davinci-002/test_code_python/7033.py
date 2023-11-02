def solution():
    total_hours = 9
    hours_for_first_guard = 3
    hours_for_last_guard = 2
    hours_for_middle_guards = total_hours - hours_for_first_guard - hours_for_last_guard
    result = hours_for_middle_guards / 2
    return result

print(solution())