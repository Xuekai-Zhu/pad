def solution():
    """Julie works at a restaurant that pays her an hourly rate of $5. She works 8 hours a day and 6 days a week. How much is her monthly salary if she was not able to go to work for a day?"""
    hourly_rate = 5
    work_hours_per_day = 8
    work_days_per_week = 6
    total_work_hours = work_hours_per_day * work_days_per_week * 4
    missed_day = work_hours_per_day * hourly_rate
    monthly_salary = (total_work_hours * hourly_rate) - missed_day
    result = monthly_salary
    return result

print(solution())