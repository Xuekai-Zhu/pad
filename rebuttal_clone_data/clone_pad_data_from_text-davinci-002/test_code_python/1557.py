def solution():
    minutes_allowed = 200
    minutes_tanning = 30
    days_tanning = 2
    weeks_in_month = 4
    days_in_week = 7
    first_two_weeks = minutes_tanning * days_tanning * 2
    last_two_weeks = minutes_allowed - first_two_weeks
    minutes_tanning_last_two_weeks = last_two_weeks / (days_tanning * 2)
    result = minutes_tanning_last_two_weeks
    
    return result

print(solution())