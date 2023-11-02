def solution():
    """Damien jogs 5 miles per day on weekdays only. How many miles does he run over three weeks?"""
    # Define the number of weekdays per week and the number of weeks
    WEEKDAYS_PER_WEEK = 5
    WEEKS = 3

    # Define the number of miles Damien jogs per day
    MILES_PER_DAY = 5

    # Calculate the total number of weekdays over three weeks
    total_weekdays = WEEKDAYS_PER_WEEK * WEEKS

    # Calculate the total number of miles Damien jogs over three weeks
    total_miles = total_weekdays * MILES_PER_DAY

    # Return the result
    result = total_miles
    return result

print(solution())