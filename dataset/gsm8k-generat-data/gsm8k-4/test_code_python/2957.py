def solution():
    """Tim sleeps 6 hours per day for 5 days a week and 10 hours a day for the other 2.  How much total sleep does he get?"""
    # Calculate the total sleep during the weekdays
    weekday_sleep = 6 * 5

    # Calculate the total sleep during the weekend
    weekend_sleep = 10 * 2

    # Calculate the total sleep for the entire week
    total_sleep = weekday_sleep + weekend_sleep

    # return the result
    result = total_sleep
    return result

print(solution())