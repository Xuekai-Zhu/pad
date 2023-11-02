def solution():
    """Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"""
    # Define the hourly rate and the time spent babysitting in minutes
    HOURLY_RATE = 12
    TIME_IN_MINUTES = 50

    # Convert the time spent babysitting to hours (rounded to 2 decimal places)
    time_in_hours = round(TIME_IN_MINUTES / 60, 2)

    # Calculate the total amount earned (rounded to 2 decimal places)
    total_earned = round(time_in_hours * HOURLY_RATE, 2)

    # Return the result
    result = total_earned
    return result

print(solution())