def solution():
    
    hourly_salary = 8.5
    daily_hours = 8
    work_days_per_month = 20
    monthly_salary = hourly_salary * daily_hours * work_days_per_month
    annual_salary = monthly_salary * 12
    result = annual_salary
    return result

print(solution())