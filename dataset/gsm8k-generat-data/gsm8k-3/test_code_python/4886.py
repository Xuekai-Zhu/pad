def solution():
    """Tom dances 4 times a week for 2 hours at a time and does this every year for 10 years.  How many hours did he dance?"""
    # Define the number of times Tom dances per week and the number of hours per dance session
    TIMES_PER_WEEK = 4
    HOURS_PER_SESSION = 2

    # Calculate the total number of hours Tom dances in a year
    hours_per_year = TIMES_PER_WEEK * HOURS_PER_SESSION * 52

    # Calculate the total number of hours Tom dances in 10 years
    total_hours = hours_per_year * 10

    # Display the total number of hours Tom dances
    result = total_hours
    return result

print(solution())