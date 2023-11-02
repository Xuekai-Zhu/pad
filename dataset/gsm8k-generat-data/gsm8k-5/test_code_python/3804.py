def solution():
    current_sleep = 4  # Corveus currently sleeps for 4 hours a day
    recommended_sleep = 6  # Corveus' doctor recommends he sleeps for 6 hours a day
    days_per_week = 7

    # Calculate the total hours Corveus currently sleeps in a week
    weekly_sleep_current = current_sleep * days_per_week

    # Calculate the total hours Corveus should sleep in a week based on his doctor's recommendation
    weekly_sleep_recommended = recommended_sleep * days_per_week

    # Calculate the total hours of sleep that Corveus lacks in a week
    sleep_lack = weekly_sleep_recommended - weekly_sleep_current
    result = sleep_lack
    return result

print(solution())