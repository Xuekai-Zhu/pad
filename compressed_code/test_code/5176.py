def solution():
    
    week_days_sleep = 6 * 5
    weekend_sleep = 9 * 2
    nap_time = 1 * 2
    total_sleep_per_week = week_days_sleep + weekend_sleep + nap_time
    total_sleep_4_weeks = total_sleep_per_week * 4
    result = total_sleep_4_weeks
    return result

print(solution())