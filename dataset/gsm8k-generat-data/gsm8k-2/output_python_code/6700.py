def solution():
    """From Sunday to Thursday, Prudence sleeps 6 hours a night. Friday and Saturday she sleeps for 9 hours a night. She also takes a 1-hour nap on Saturday and Sunday. How much sleep does she get in 4 weeks?"""
    week_days_sleep = 6 * 5
    weekend_sleep = 9 * 2
    nap_time = 1 * 2
    total_sleep_per_week = week_days_sleep + weekend_sleep + nap_time
    total_sleep_4_weeks = total_sleep_per_week * 4
    result = total_sleep_4_weeks
    return result

print(solution())