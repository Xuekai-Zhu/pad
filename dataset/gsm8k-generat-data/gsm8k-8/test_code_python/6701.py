def solution():
    # Calculate total sleep per night from Sunday to Thursday
    weekday_sleep = 6 * 5

    # Calculate total sleep per night for Friday and Saturday
    weekend_sleep = 9 * 2

    # Calculate total nap time for Saturday and Sunday
    weekend_nap = 1 * 2

    # Calculate total sleep per week
    total_sleep_weekly = weekday_sleep + weekend_sleep + weekend_nap

    # Calculate total sleep in 4 weeks
    total_sleep_four_weeks = total_sleep_weekly * 4

    result = total_sleep_four_weeks
    return result

print(solution())