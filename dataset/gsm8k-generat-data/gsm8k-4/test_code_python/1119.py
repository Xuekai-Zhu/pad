def solution():
    """Jill spends time every day talking to her boyfriend on the phone. The first day of the week she spends 5 minutes on the phone with her boyfriend. Each of the following days she spends twice as much time talking on the phone as the day before. After the 5th day her parents take the phone away from her because she was on it too long. How much time did Jill spend talking to her boyfriend that week?"""
    # Initialize the total time spent on the phone
    total_time = 5

    # Initialize the time spent on the phone each day
    daily_time = 5

    # Calculate the total time spent on the phone for the rest of the week
    for i in range(2, 6):
        # Double the time spent on the phone each day
        daily_time *= 2

        # Add the daily time to the total time
        total_time += daily_time

    # Display the total time spent on the phone
    result = total_time
    return result

print(solution())