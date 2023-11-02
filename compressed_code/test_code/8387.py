def solution():
    
    minutes_per_weekday = 30 * 5
    minutes_per_weekend = 2 * 60
    minutes_per_week = minutes_per_weekday + minutes_per_weekend
    minutes_per_year = minutes_per_week * 52
    hours_per_year = minutes_per_year / 60
    result = hours_per_year
    return result

print(solution())