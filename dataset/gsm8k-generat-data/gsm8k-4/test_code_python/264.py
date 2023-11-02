def solution():
    """An Italian restaurant earns $600 every weekday and twice as much on the weekend. How much money does it earn by the end of the month?"""
    # Define the earnings per weekday and weekend day
    weekday_earnings = 600
    weekend_earnings = 2 * weekday_earnings

    # Calculate the earnings for a month (assume 30 days in a month)
    month_earnings = (5 * weekday_earnings + 2 * weekend_earnings) * 30

    result = month_earnings
    return result

print(solution())