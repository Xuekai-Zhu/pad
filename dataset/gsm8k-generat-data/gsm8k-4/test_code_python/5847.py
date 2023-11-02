def solution():
    """Ursula earns $8.50 an hour working in a restaurant. She works 8 hours a day. If she works 20 days a month, determine her annual salary."""
    # Define the hourly wage and number of hours worked per day
    HOURLY_WAGE = 8.5
    HOURS_PER_DAY = 8

    # Define the number of days worked per month
    DAYS_PER_MONTH = 20

    # Calculate the monthly salary
    monthly_salary = HOURLY_WAGE * HOURS_PER_DAY * DAYS_PER_MONTH

    # Calculate the annual salary
    annual_salary = monthly_salary * 12

    # return the result
    result = annual_salary
    return result

print(solution())