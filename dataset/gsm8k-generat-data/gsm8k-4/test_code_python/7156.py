def solution():
    """Rich ran a 24-mile marathon in 3 hours and 36 minutes. On average, how long, in minutes, did it take Rich to run a mile during the race?"""
    # Define the total distance and time
    distance = 24
    time_hours = 3
    time_minutes = 36

    # Convert the time to minutes
    total_time_minutes = time_hours * 60 + time_minutes

    # Calculate the average time per mile
    time_per_mile = total_time_minutes / distance

    # Round the result to two decimal places and return it
    result = round(time_per_mile, 2)
    return result

print(solution())