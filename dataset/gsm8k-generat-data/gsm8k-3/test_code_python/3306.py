def solution():
    """Larry jogs for 30 minutes each day. In the first week, he jogs for 3 days while he jogs for 5 days in the second week. How many hours does he jog in total for two weeks?"""
    # Define the number of days in each week and the jogging time per day
    DAYS_WEEK1 = 3
    DAYS_WEEK2 = 5
    JOGGING_TIME = 30/60   # Convert 30 minutes to hours

    # Calculate the total jogging time in hours
    total_jogging_time = (DAYS_WEEK1 + DAYS_WEEK2) * JOGGING_TIME

    # Display the total jogging time
    result = total_jogging_time
    return result

print(solution())