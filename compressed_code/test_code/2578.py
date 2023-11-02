def solution():
    
    total_school_days = 180
    allowed_missed_days = total_school_days * 0.05
    remaining_allowed_missed_days = allowed_missed_days - 6
    result = remaining_allowed_missed_days
    return result

print(solution())