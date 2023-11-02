def solution():
    weekday_hours = 5
    weekend_hours = 3
    hourly_rate = 3

    # Calculate the total earnings for weekdays
    weekday_earnings = weekday_hours * hourly_rate * 5

    # Calculate the total earnings for weekends
    weekend_earnings = weekend_hours * hourly_rate * 2 * 2  # double pay for weekends, and there are two weekend days

    # Calculate the total earnings for the whole week
    total_earnings = weekday_earnings + weekend_earnings
    result = total_earnings
    return result

print(solution())