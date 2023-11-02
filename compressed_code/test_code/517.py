def solution():
    
    week_days = 5
    weekend_days = 2
    nightly_hours = 2
    weekend_hours = 3
    total_weeks = 6
    total_weekday_hours = nightly_hours * week_days
    total_weekend_hours = weekend_hours * weekend_days
    total_study_hours = (total_weekday_hours + total_weekend_hours) * total_weeks
    result = total_study_hours
    return result

print(solution())