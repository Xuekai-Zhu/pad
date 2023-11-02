def solution():
    
    total_attempts = 60
    missed_percentage = 1/4
    missed_field_goals = total_attempts * missed_percentage
    wide_right_percentage = 0.2
    wide_right_misses = missed_field_goals * wide_right_percentage
    result = wide_right_misses
    return result

print(solution())