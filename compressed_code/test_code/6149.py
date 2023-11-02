def solution():
    
    gym_hours_per_day = 1
    gym_days_per_week = 3
    boxing_hours_per_day = 1.5
    boxing_days_per_week = 4
    total_gym_hours = gym_hours_per_day * gym_days_per_week
    total_boxing_hours = boxing_hours_per_day * boxing_days_per_week
    total_hours = total_gym_hours + total_boxing_hours
    result = total_hours
    return result

print(solution())