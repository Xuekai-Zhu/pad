def solution():
    """From Sunday to Thursday, Prudence sleeps 6 hours a night. Friday and Saturday she sleeps for 9 hours a night. She also takes a 1-hour nap on Saturday and Sunday. How much sleep does she get in 4 weeks?"""
    weekday_sleep = 6 * 5
    weekend_sleep = 9 * 2
    nap_time = 1 * 2
    total_sleep = (weekday_sleep + weekend_sleep + nap_time) * 4
    result = total_sleep
    return result

print(solution())