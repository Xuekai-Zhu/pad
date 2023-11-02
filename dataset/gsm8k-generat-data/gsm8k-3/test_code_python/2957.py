def solution():
    """Tim sleeps 6 hours per day for 5 days a week and 10 hours a day for the other 2.  How much total sleep does he get?"""
    # Calculate the total number of hours slept during the weekdays
    weekday_hours = 6 * 5

    # Calculate the total number of hours slept during the weekend
    weekend_hours = 10 * 2

    # Calculate the total number of hours slept in a week
    total_hours = weekday_hours + weekend_hours

    # Display the total number of hours slept
    result = total_hours
    return result

print(solution())