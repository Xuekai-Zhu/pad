def solution():
    """Jeff committed to run for an hour a day during weekdays. On Thursday, he cut short his run by 20 minutes but was able to jog 10 minutes more on Friday. How many minutes was he able to run for that week?"""
    # Define the number of minutes Jeff runs per day
    DAILY_RUN_TIME = 60

    # Define the number of days Jeff runs per week
    WEEKLY_RUN_DAYS = 5

    # Calculate the total number of minutes Jeff runs from Monday to Friday
    total_run_time = DAILY_RUN_TIME * WEEKLY_RUN_DAYS

    # Subtract the 20-minute cut on Thursday and add the 10-minute addition on Friday
    adjusted_total_run_time = total_run_time - 20 + 10

    # Display the total number of minutes Jeff was able to run for the week
    result = adjusted_total_run_time
    return result

print(solution())