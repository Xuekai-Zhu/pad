def solution():
    """Ludwig works 7 days a week and he usually works half of the day during Friday, Saturday, and Sunday. If his daily salary is $10, how much does he earn every week?"""
    # Define the daily salary and the number of working days
    daily_salary = 10
    working_days = 7 - 3*0.5

    # Calculate the weekly earnings
    weekly_earnings = daily_salary * working_days

    # return the result
    result = weekly_earnings
    return result

print(solution())