def solution():
    """Ludwig works 7 days a week and he usually works half of the day during Friday, Saturday, and Sunday.
    If his daily salary is $10, how much does he earn every week?"""
    daily_salary = 10
    full_day_work = 4 * daily_salary
    half_day_work = 2 * daily_salary
    weekly_salary = (full_day_work * 4) + (half_day_work * 3)
    result = weekly_salary
    return result

print(solution())