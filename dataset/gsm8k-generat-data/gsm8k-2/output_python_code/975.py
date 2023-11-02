def solution():
    """Ludwig works 7 days a week and he usually works half of the day during Friday, Saturday, and Sunday. If his daily salary is $10, how much does he earn every week?"""
    daily_salary = 10
    weekdays_worked = 4  # assuming he works full days Monday-Thursday
    weekend_worked_hours = 12  # assuming he works half days Friday-Sunday
    weekly_salary = (daily_salary * weekdays_worked) + (daily_salary/2 * weekend_worked_hours)
    result = weekly_salary
    return result

print(solution())