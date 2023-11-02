def solution():
    """Sherman has a 30-minute commute to the office and a 30-minute commute home every day. On the weekends, he spends 2 hours, each day, driving his kids to their different activities. How many hours does Sherman drive a week?"""
    # Calculate the daily commute time
    daily_commute = 30 + 30  # minutes

    # Calculate the weekend driving time
    weekend_driving = 2 * 60  # minutes

    # Calculate the total driving time for the week
    weekly_driving = daily_commute * 5 + weekend_driving * 2  # minutes
    weekly_driving /= 60  # convert to hours

    # Return the result
    result = weekly_driving
    return result

print(solution())