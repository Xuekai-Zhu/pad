def solution():
    """Janna sleeps 7 hours each day during weekdays and 8 hours each day during weekends. How many hours does she sleep in a week?"""
    # Define the number of hours Janna sleeps each day
    weekday_hours = 7
    weekend_hours = 8

    # Calculate the total hours Janna sleeps during a week, assuming 5 weekdays and 2 weekends
    total_hours = (weekday_hours * 5) + (weekend_hours * 2)

    # Return the result
    result = total_hours
    return result

print(solution())