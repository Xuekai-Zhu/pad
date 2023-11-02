def solution():
    """Mr. John jogs for 1 hour 30 minutes in the morning every day. How much time (in hours) will he have spent jogging after two weeks?"""
    # Define the time Mr. John spends jogging per day
    time_per_day = 1.5     # in hours

    # Calculate the total time spent jogging in two weeks (14 days)
    total_time = time_per_day * 14

    # Convert the total time to hours
    total_time_hours = total_time / 60

    # Return the result
    result = total_time_hours
    return result

print(solution())