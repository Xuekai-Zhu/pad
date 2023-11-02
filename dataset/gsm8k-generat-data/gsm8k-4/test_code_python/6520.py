def solution():
    """Doris earns $20 per hour by babysitting. She needs to earn at least $1200 for her monthly expenses. She can babysit for 3 hours every weekday and 5 hours on a Saturday.  How many weeks does it take for Doris to earn enough to cover her monthly expenses?"""
    # Define the hourly rate and the required monthly income
    hourly_rate = 20
    required_income = 1200

    # Calculate the income earned per week
    daily_income = 3 * hourly_rate * 5  # 3 hours every weekday, 5 weekdays in a week
    saturday_income = 5 * hourly_rate  # 5 hours on a Saturday
    weekly_income = daily_income + saturday_income

    # Calculate the number of weeks required to earn the required income
    weeks = required_income / weekly_income

    # Round up to the nearest integer
    weeks = math.ceil(weeks)

    # Return the result
    result = weeks
    return result

print(solution())