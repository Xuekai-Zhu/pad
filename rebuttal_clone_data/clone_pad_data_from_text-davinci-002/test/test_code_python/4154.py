def solution():
    newspaper_minutes_per_day = 30
    novel_minutes_per_day = 60
    reading_minutes_per_weekday = newspaper_minutes_per_day + novel_minutes_per_day
    reading_minutes_per_weekend_day = reading_minutes_per_weekday * 2
    total_reading_minutes_per_week = reading_minutes_per_weekday * 5 + reading_minutes_per_weekend_day * 2
    result = total_reading_minutes_per_week
    
    return result

print(solution())