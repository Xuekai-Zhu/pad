def solution():
    """Last week, Arman worked 35 hours for 5 days at $10 per hour. This week, he will receive an increase of $0.5 per hour if he can work for 40 hours. Suppose he can work for 40 hours this week, how much will Arman receive for working two weeks?"""
    # Define Arman's hourly rate and weekly hours
    hourly_rate = 10
    weekly_hours = 35

    # Calculate Arman's earnings from last week
    last_week_earnings = hourly_rate * weekly_hours

    # Calculate Arman's earnings for this week, with the increased hourly rate
    increased_hourly_rate = hourly_rate + 0.5
    this_week_earnings = increased_hourly_rate * 40

    # Calculate Arman's total earnings for two weeks
    total_earnings = last_week_earnings + this_week_earnings

    # return the result
    result = total_earnings
    return result

print(solution())