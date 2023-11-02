def solution():
    
    hourly_rate = 5
    work_hours_per_day = 8
    work_days_per_week = 6
    monthly_salary = hourly_rate * work_hours_per_day * work_days_per_week * 4
    daily_salary = monthly_salary / 24  
    salary_with_absence = monthly_salary - daily_salary
    result = salary_with_absence
    return result

print(solution())