def solution():
    
    school_week_duration = 5
    school_week_minutes = school_week_duration * 15
    weekend_duration = 2
    weekend_minutes = weekend_duration * 15 * 2
    total_minutes = school_week_minutes + weekend_minutes
    result = total_minutes
    return result

print(solution())