def solution():
    """Corveus sleeps 4 hours a day and his doctor recommended for him to sleep 6 hours a day. How many hours of sleep does Corveus lack in a week?"""
    # Define the number of hours of recommended sleep per day and the number of days in a week
    RECOMMENDED_SLEEP = 6
    DAYS_IN_WEEK = 7

    # Define the number of hours of sleep Corveus gets per day
    corveus_sleep = 4

    # Calculate the number of hours of sleep Corveus lacks per day
    sleep_lack_per_day = RECOMMENDED_SLEEP - corveus_sleep

    # Calculate the total number of hours of sleep Corveus lacks in a week
    sleep_lack_per_week = sleep_lack_per_day * DAYS_IN_WEEK

    # Display the total number of hours of sleep Corveus lacks in a week
    result = sleep_lack_per_week
    return result

print(solution())