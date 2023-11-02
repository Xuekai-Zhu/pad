def solution():
    
    hourly_rate = 13.50
    regular_hours_per_day = 8
    overtime_hours_per_day = 2
    workdays_per_week = 5
    regular_weekly_pay = hourly_rate * regular_hours_per_day * workdays_per_week
    overtime_weekly_pay = hourly_rate * overtime_hours_per_day * workdays_per_week
    total_weekly_pay = regular_weekly_pay + overtime_weekly_pay
    result = total_weekly_pay
    return result

print(solution())