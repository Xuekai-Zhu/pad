def solution():
    """Larry jogs for 30 minutes each day. In the first week, he jogs for 3 days while he jogs for 5 days in the second week. How many hours does he jog in total for two weeks?"""
    # Define the time Larry jogs each day in minutes
    JOG_TIME = 30

    # Calculate the total time Larry jogs in the first week
    week1_jog = JOG_TIME * 3

    # Calculate the total time Larry jogs in the second week
    week2_jog = JOG_TIME * 5

    # Calculate the total time Larry jogs in two weeks in hours
    total_jog_hours = (week1_jog + week2_jog) / 60

    # Return the result
    result = total_jog_hours
    return result

print(solution())