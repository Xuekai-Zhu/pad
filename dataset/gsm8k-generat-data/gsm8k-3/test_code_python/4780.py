def solution():
    """Last week, Arman worked 35 hours for 5 days at $10 per hour. This week, he will receive an increase of $0.5 per hour if he can work for 40 hours. Suppose he can work for 40 hours this week, how much will Arman receive for working two weeks?"""
    # Define Arman's hourly rate and the number of hours worked last week and this week
    HOURLY_RATE = 10
    HOURS_LAST_WEEK = 35
    HOURS_THIS_WEEK = 40

    # Calculate Arman's earnings for last week
    earnings_last_week = HOURLY_RATE * HOURS_LAST_WEEK * 5

    # Calculate Arman's earnings for this week
    if HOURS_THIS_WEEK >= 40:
        hourly_rate_this_week = HOURLY_RATE + 0.5
        earnings_this_week = hourly_rate_this_week * HOURS_THIS_WEEK
    else:
        earnings_this_week = HOURLY_RATE * HOURS_THIS_WEEK

    # Calculate Arman's total earnings for the two weeks
    total_earnings = earnings_last_week + earnings_this_week

    # Display Arman's total earnings
    result = total_earnings
    return result

print(solution())