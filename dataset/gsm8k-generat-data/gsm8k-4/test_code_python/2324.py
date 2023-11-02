def solution():
    """Isabella earns $5 an hour babysitting. She babysits 5 hours every day, 6 afternoons a week. After babysitting for 7 weeks, how much money will Isabella have earned?"""
    # Define the hourly wage and the number of hours worked per day and per week
    HOURLY_WAGE = 5
    DAILY_HOURS = 5
    WEEKLY_AFTERNOONS = 6

    # Calculate the total number of hours worked in 7 weeks
    total_hours = DAILY_HOURS * WEEKLY_AFTERNOONS * 7

    # Calculate the total earnings
    total_earnings = total_hours * HOURLY_WAGE

    # Return the result
    result = total_earnings
    return result

print(solution())