def solution():
    
    daily_sports_hours = 2
    school_days_per_week = 5
    missed_days = 2
    total_days = school_days_per_week - missed_days
    total_sports_hours = daily_sports_hours * total_days
    result = total_sports_hours
    return result

print(solution())