def solution():
    """Julie works at a restaurant that pays her an hourly rate of $5. She works 8 hours a day and 6 days a week. How much is her monthly salary if she was not able to go to work for a day?"""
    # Define the hourly rate and number of working hours per week
    HOURLY_RATE = 5
    WEEKLY_HOURS = 8 * 6

    # Calculate the monthly salary without the missed day
    monthly_salary = WEEKLY_HOURS * HOURLY_RATE * 4

    # Calculate the daily salary and subtract it from the monthly salary
    daily_salary = WEEKLY_HOURS * HOURLY_RATE
    missed_day_salary = daily_salary * 1
    monthly_salary -= missed_day_salary

    # Display the monthly salary
    result = monthly_salary
    return result

print(solution())