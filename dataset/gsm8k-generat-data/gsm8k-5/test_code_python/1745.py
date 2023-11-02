def solution():
    agnes_hourly_salary = 15  # Agnes makes $15 per hour
    agnes_weekly_hours = 8  # Agnes works 8 hours each week
    agnes_monthly_salary = agnes_hourly_salary * agnes_weekly_hours * 4  # Agnes works for 4 weeks in a month

    mila_hourly_salary = 10  # Mila makes $10 per hour
    mila_monthly_salary = agnes_monthly_salary  # Mila wants to earn as much as Agnes in a month

    # Calculate how many hours Mila needs to work to earn as much as Agnes
    mila_monthly_hours = mila_monthly_salary / mila_hourly_salary
    result = mila_monthly_hours
    return result

print(solution())