def solution():
    
    monthly_salary = 576
    hours_per_day = 8
    days_per_week = 6
    weeks_per_month = 4
    total_hours_worked = hours_per_day * days_per_week * weeks_per_month
    hourly_rate = monthly_salary / total_hours_worked
    result = hourly_rate
    return result

print(solution())