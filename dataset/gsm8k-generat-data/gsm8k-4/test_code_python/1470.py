def solution():
    """Ayen jogs for 30 minutes every day during weekdays. This week on Tuesday, she jogged 5 minutes more and also jogged 25 minutes more on Friday. How many hours, in total, did Ayen jog this week?"""
    # Define the amount of time Ayen jogs each weekday
    daily_jog_time = 30

    # Calculate the total amount of time Ayen jogs from Monday to Thursday
    total_jog_time = daily_jog_time * 4

    # Add the additional time on Tuesday and Friday
    total_jog_time += 5 + 30 + 25

    # Convert the total jog time from minutes to hours
    total_jog_time_hours = total_jog_time / 60

    result = round(total_jog_time_hours, 2)
    return result

print(solution())