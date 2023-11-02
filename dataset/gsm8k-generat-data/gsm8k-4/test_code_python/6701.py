def solution():
    """From Sunday to Thursday, Prudence sleeps 6 hours a night. Friday and Saturday she sleeps for 9 hours a night. She also takes a 1-hour nap on Saturday and Sunday. How much sleep does she get in 4 weeks?"""
    # Define the hours of sleep per night and nap
    weekday_sleep = 6
    weekend_sleep = 9
    nap_sleep = 1

    # Calculate the total hours of sleep in a day
    total_sleep = (weekday_sleep * 5) + (weekend_sleep * 2) + (nap_sleep * 2)

    # Calculate the total hours of sleep in 4 weeks (28 days)
    total_sleep_four_weeks = total_sleep * 28

    # return the result
    result = total_sleep_four_weeks
    return result

print(solution())