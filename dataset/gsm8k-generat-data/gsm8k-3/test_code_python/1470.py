def solution():
    """Ayen jogs for 30 minutes every day during weekdays. This week on Tuesday, she jogged 5 minutes more and also jogged 25 minutes more on Friday. How many hours, in total, did Ayen jog this week?"""
    # Define the number of minutes Ayen jogs per day during weekdays
    DAILY_JOG_TIME = 30

    # Calculate the total number of minutes Ayen jogged this week
    total_jog_time = (4 * DAILY_JOG_TIME) + (DAILY_JOG_TIME + 5) + (DAILY_JOG_TIME + 25)

    # Convert the total jog time to hours
    total_jog_time_hours = total_jog_time / 60

    # Display the total jog time in hours
    result = total_jog_time_hours
    return result

print(solution())