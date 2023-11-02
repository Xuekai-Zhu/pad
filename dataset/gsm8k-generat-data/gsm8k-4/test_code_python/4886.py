def solution():
    """Tom dances 4 times a week for 2 hours at a time and does this every year for 10 years. How many hours did he dance?"""
    # Define the number of times Tom dances per week and the duration of each dance
    times_per_week = 4
    duration_per_dance = 2

    # Define the number of years Tom dances
    years = 10

    # Calculate the total number of hours Tom dances
    total_hours = times_per_week * duration_per_dance * 52 * years

    # Return the result
    result = total_hours
    return result

print(solution())