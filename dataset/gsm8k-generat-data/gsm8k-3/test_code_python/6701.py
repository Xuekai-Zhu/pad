def solution():
    """From Sunday to Thursday, Prudence sleeps 6 hours a night.  Friday and Saturday she sleeps for 9 hours a night.  She also takes a 1-hour nap on Saturday and Sunday.  How much sleep does she get in 4 weeks?"""
    # Define the number of days in a week and the number of weeks
    DAYS_IN_WEEK = 7
    WEEKS = 4

    # Calculate the number of hours of sleep Prudence gets from Sunday to Thursday
    weekday_sleep = 6 * (DAYS_IN_WEEK - 2) * WEEKS

    # Calculate the number of hours of sleep Prudence gets on Friday and Saturday
    weekend_sleep = 9 * 2 * WEEKS

    # Calculate the number of hours of naps Prudence takes on Saturday and Sunday
    weekend_naps = 1 * 2 * WEEKS

    # Calculate the total number of hours of sleep Prudence gets in 4 weeks
    total_sleep = weekday_sleep + weekend_sleep + weekend_naps

    # Display the total number of hours of sleep Prudence gets
    result = total_sleep
    return result

print(solution())