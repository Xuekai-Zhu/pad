def solution():
    """Tim sleeps 6 hours per day for 5 days a week and 10 hours a day for the other 2. How much total sleep does he get?"""
    weekday_sleep = 6 * 5
    weekend_sleep = 10 * 2
    total_sleep = weekday_sleep + weekend_sleep
    result = total_sleep
    return result

print(solution())