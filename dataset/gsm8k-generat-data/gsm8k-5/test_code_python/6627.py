def solution():
    recommended_sleep = 8  # Recommended hours of sleep per day
    days_with_only_3_hours = 2  # Number of days John slept only 3 hours
    days_with_60_percent_sleep = 7 - days_with_only_3_hours  # Number of days John slept 60% of recommended sleep

    total_hours_of_sleep = (days_with_only_3_hours * 3) + (days_with_60_percent_sleep * 0.6 * recommended_sleep * 7)
    result = total_hours_of_sleep
    return result

print(solution())