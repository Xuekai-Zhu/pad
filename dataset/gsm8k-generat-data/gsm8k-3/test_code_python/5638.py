def solution():
    """Janna sleeps 7 hours each day during weekdays and 8 hours each day during weekends. How many hours does she sleep in a week?"""
    # Define the number of hours Janna sleeps during weekdays and weekends
    WEEKDAY_SLEEP_HOURS = 7
    WEEKEND_SLEEP_HOURS = 8

    # Calculate the total number of hours Janna sleeps in a week
    total_sleep_hours = (WEEKDAY_SLEEP_HOURS * 5) + (WEEKEND_SLEEP_HOURS * 2)

    # Display the total number of hours Janna sleeps in a week
    result = total_sleep_hours
    return result

print(solution())