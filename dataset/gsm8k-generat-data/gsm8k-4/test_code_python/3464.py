def solution():
    """Lisa walks 10 meters each minute. Every day, she walks for an hour. How many meters will Lisa walk in two days?"""
    # Define the distance Lisa walks in one minute and one hour
    meters_per_minute = 10
    meters_per_hour = meters_per_minute * 60

    # Calculate the total distance Lisa walks in two days
    total_meters = meters_per_hour * 2

    # Return the result
    result = total_meters
    return result

print(solution())