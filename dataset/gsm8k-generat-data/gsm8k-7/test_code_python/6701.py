def solution():
    # Calculate the total hours of sleep per week
    weekdays_sleep = 6 * 5
    weekend_sleep = 9 * 2
    nap_sleep = 1 * 2
    total_sleep_per_week = weekdays_sleep + weekend_sleep + nap_sleep

    # Calculate the total hours of sleep per month
    total_sleep_per_month = total_sleep_per_week * 4
    result = total_sleep_per_month
    return result

print(solution())