def solution():
    """Lisa walks 10 meters each minute. Every day, she walks for an hour. How many meters will Lisa walk in two days?"""
    # Define the meters Lisa walks per minute and the number of minutes she walks per day
    METERS_PER_MINUTE = 10
    MINUTES_PER_DAY = 60

    # Calculate the number of meters Lisa walks per day
    meters_per_day = METERS_PER_MINUTE * MINUTES_PER_DAY

    # Calculate the total number of meters Lisa will walk in two days
    total_meters = meters_per_day * 2

    # Display the total number of meters
    result = total_meters
    return result

print(solution())