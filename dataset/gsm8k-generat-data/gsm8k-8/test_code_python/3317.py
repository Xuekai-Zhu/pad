def solution():
    total_school_days = 180
    max_missed_days = total_school_days * 0.05
    current_missed_days = 6

    remaining_missed_days = max_missed_days - current_missed_days
    result = remaining_missed_days
    return result

print(solution())