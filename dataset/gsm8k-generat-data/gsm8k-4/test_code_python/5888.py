def solution():
    """Julie works at a restaurant that pays her an hourly rate of $5. She works 8 hours a day and 6 days a week. How much is her monthly salary if she was not able to go to work for a day?"""
    # Define Julie's hourly rate, number of work hours per day, and number of work days per week
    hourly_rate = 5
    work_hours_per_day = 8
    work_days_per_week = 6

    # Calculate Julie's monthly salary without the missed day of work
    monthly_salary = hourly_rate * work_hours_per_day * work_days_per_week * 4

    # Calculate Julie's daily salary
    daily_salary = hourly_rate * work_hours_per_day

    # Calculate Julie's monthly salary with the missed day of work
    monthly_salary_missed_day = monthly_salary - daily_salary

    result = monthly_salary_missed_day
    return result

print(solution())