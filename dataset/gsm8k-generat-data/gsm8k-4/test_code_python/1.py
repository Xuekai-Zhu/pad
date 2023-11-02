def solution():
    """Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"""
    # Define Weng's hourly rate and the time she spent babysitting
    HOURLY_RATE = 12
    TIME_IN_MINUTES = 50

    # Calculate Weng's earnings based on the time spent babysitting
    earnings = (TIME_IN_MINUTES / 60) * HOURLY_RATE

    # Return the result
    result = earnings
    return result

print(solution())