def solution():
    
    daily_distance = 140
    days_per_week = 7
    work_days_per_week = days_per_week - 3
    total_distance_per_week = daily_distance * work_days_per_week
    total_distance_per_four_weeks = total_distance_per_week * 4
    result = total_distance_per_four_weeks
    return result

print(solution())