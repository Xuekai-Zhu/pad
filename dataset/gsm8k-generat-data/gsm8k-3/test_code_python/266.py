def solution():
    """An Italian restaurant earns $600 every weekday and twice as much on the weekend. How much money does it earn by the end of the month?"""
    # Define the daily earnings
    WEEKDAY_EARNINGS = 600

    # Calculate the total earnings for the weekdays in a month (assuming 4 weeks)
    weekday_total = WEEKDAY_EARNINGS * 5 * 4

    # Calculate the total earnings for the weekends in a month (assuming 4 weekends)
    weekend_total = 2 * weekday_total

    # Calculate the total earnings for the month
    total_earnings = weekday_total + weekend_total

    # Display the total earnings
    result = total_earnings
    return result

print(solution())