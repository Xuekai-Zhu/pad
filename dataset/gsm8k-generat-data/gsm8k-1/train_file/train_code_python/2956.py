def solution():
    """Tim sleeps 6 hours per day for 5 days a week and 10 hours a day for the other 2. How much total sleep does he get?"""
    hours_sleep_weekdays = 6 * 5
    hours_sleep_weekends = 10 * 2
    total_sleep = hours_sleep_weekdays + hours_sleep_weekends
    result = total_sleep
    return result

print(solution())