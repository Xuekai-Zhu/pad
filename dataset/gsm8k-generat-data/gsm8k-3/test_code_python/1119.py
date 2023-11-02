def solution():
    """Jill spends time every day talking to her boyfriend on the phone.  The first day of the week she spends 5 minutes on the phone with her boyfriend.  Each of the following days she spends twice as much time talking on the phone as the day before. After the 5th day her parents take the phone away from her because she was on it too long.  How much time did Jill spend talking to her boyfriend that week?"""
    # Define the initial phone call time and the total time
    first_day_time = 5
    total_time = 5

    # Loop through the remaining days of the week
    for i in range(2, 6):
        # Calculate the phone call time for the current day
        current_day_time = first_day_time * (2 ** (i - 1))
        # Add the current day's phone call time to the total time
        total_time += current_day_time

    # Display the total time
    result = total_time
    return result

print(solution())