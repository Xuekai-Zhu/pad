def solution():
    
    videos_per_week = 18
    hours_per_week = 2
    minutes_per_week_writing_amateur = hours_per_week * 60
    minutes_per_week_makeup = 15 * 6
    total_minutes_per_week = videos_per_week * minutes_per_week_writing_amateur + minutes_per_week_makeup
    total_minutes_per_month = total_minutes_per_week * 4
    result = total_minutes_per_month
    return result

print(solution())