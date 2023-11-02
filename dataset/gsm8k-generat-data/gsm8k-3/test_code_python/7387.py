def solution():
    """Jose threatened to withhold 20% of Amanda's pay if she does not finish her sales report by midnight. If Amanda makes $50.00 an hour and works for 10 hours a day, how much money will she receive if she does not finish the sales report by midnight?"""
    # Define Amanda's hourly rate and work hours
    HOURLY_RATE = 50
    WORK_HOURS = 10

    # Calculate Amanda's daily earnings
    daily_earnings = HOURLY_RATE * WORK_HOURS

    # Calculate the amount withheld if Amanda does not finish the report
    withholding_amount = daily_earnings * 0.2

    # Calculate Amanda's earnings for the day after withholding
    earnings_after_withholding = daily_earnings - withholding_amount

    # Display Amanda's earnings
    result = earnings_after_withholding
    return result

print(solution())