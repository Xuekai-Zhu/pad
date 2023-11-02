def solution():
    work_days = 7
    daily_salary = 10
    half_day_salary = daily_salary / 2  # half-day salary is half of the daily salary

    # Calculate Ludwig's normal salary for 4 days (Monday to Thursday)
    normal_salary = daily_salary * (work_days - 3)  # 3 days (Friday to Sunday) are half days

    # Calculate Ludwig's weekend salary for 3 half days (Friday to Sunday)
    weekend_salary = half_day_salary * 3

    # Calculate Ludwig's total weekly salary
    total_salary = normal_salary + weekend_salary
    result = total_salary
    return result

print(solution())