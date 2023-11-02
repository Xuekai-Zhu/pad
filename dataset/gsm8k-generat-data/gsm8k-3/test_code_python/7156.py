def solution():
    """Rich ran a 24-mile marathon in 3 hours and 36 minutes. On average, how long, in minutes, did it take Rich to run a mile during the race?"""
    # Convert the time to total minutes
    total_minutes = 3 * 60 + 36

    # Calculate the average time per mile
    time_per_mile = total_minutes / 24

    # Display the time per mile in minutes
    result = time_per_mile
    return result

print(solution())