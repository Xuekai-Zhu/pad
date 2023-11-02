def solution():
    """Doris earns $20 per hour by babysitting. She needs to earn at least $1200 for her monthly expenses. She can babysit for 3 hours every weekday and 5 hours on a Saturday.  How many weeks does it take for Doris to earn enough to cover her monthly expenses?"""
    # Define the hourly rate and monthly expenses
    HOURLY_RATE = 20
    MONTHLY_EXPENSES = 1200

    # Calculate the total number of hours Doris can babysit per week
    weekly_hours = 3 * 5 + 5

    # Calculate Doris's weekly earnings
    weekly_earnings = weekly_hours * HOURLY_RATE

    # Calculate the number of weeks it takes for Doris to earn enough to cover her monthly expenses
    weeks = MONTHLY_EXPENSES / weekly_earnings

    # Display the number of weeks
    result = weeks
    return result

print(solution())