def solution():
    
    monthly_salary = 576
    work_days_per_week = 6
    work_hours_per_day = 8
    total_work_hours_per_week = work_days_per_week * work_hours_per_day
    hourly_rate = monthly_salary / (4 * total_work_hours_per_week)
    result = hourly_rate
    return result

print(solution())