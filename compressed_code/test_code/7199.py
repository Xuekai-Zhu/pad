def solution():
    
    hourly_rate = 13.50
    regular_hours_per_day = 8
    overtime_hours_per_day = 2
    days_per_week = 5
    regular_hours_per_week = regular_hours_per_day * days_per_week
    overtime_hours_per_week = overtime_hours_per_day * days_per_week
    total_hours_per_week = regular_hours_per_week + overtime_hours_per_week
    total_earnings = total_hours_per_week * hourly_rate
    result = total_earnings
    return result

print(solution())