def solution():
    """Julie works at a restaurant that pays her an hourly rate of $5. She works 8 hours a day and 6 days a week. How much is her monthly salary if she was not able to go to work for a day?"""
    hourly_rate = 5
    work_hours_per_day = 8
    work_days_per_week = 6
    monthly_salary = hourly_rate * work_hours_per_day * work_days_per_week * 4
    daily_salary = monthly_salary / 24  # assuming there are 24 work days in a month
    salary_with_absence = monthly_salary - daily_salary
    result = salary_with_absence
    return result

print(solution())