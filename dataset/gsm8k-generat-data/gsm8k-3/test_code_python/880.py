def solution():
    """Mr. John jogs for 1 hour 30 minutes in the morning every day. How much time (in hours) will he have spent jogging after two weeks?"""
    # Define the time Mr. John spends jogging daily
    DAILY_JOGGING_TIME = 1.5

    # Calculate the total time Mr. John will spend jogging in 2 weeks
    total_jogging_time = DAILY_JOGGING_TIME * 14

    # Convert the total jogging time from minutes to hours
    total_jogging_hours = total_jogging_time / 60

    # Display the total jogging time in hours
    result = total_jogging_hours
    return result

print(solution())