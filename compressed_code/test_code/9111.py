def solution():
    
    beats_per_minute = 200
    minutes_per_hour = 60
    hours_per_day = 2
    days_per_week = 7
    total_minutes = minutes_per_hour * hours_per_day * days_per_week
    total_beats = total_minutes * beats_per_minute
    result = total_beats
    return result

print(solution())