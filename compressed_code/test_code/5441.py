def solution():
    
    total_hours = 9
    first_guard = 3
    last_guard = 2
    remaining_hours = total_hours - first_guard - last_guard
    middle_guards_hours = remaining_hours / 2
    result = middle_guards_hours
    return result

print(solution())