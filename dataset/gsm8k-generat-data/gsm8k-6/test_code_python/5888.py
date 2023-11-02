def solution():
    # Calculate Julie's monthly salary without the missed day
    monthly_salary = 5 * 8 * 6 * 4  # $5 hourly rate, 8 hours a day, 6 days a week, 4 weeks in a month

    # Calculate Julie's daily salary
    daily_salary = monthly_salary / 24  # 24 working days in a month

    # Calculate Julie's salary for a missed day
    missed_day_salary = daily_salary / 8  # 8 working hours in a day

    # Subtract the missed day's salary from the monthly salary
    final_salary = monthly_salary - missed_day_salary
    result = final_salary
    return result

print(solution())