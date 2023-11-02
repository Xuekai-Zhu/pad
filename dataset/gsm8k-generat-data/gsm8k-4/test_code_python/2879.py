def solution():
    """Malcolm brushes his teeth for 2 minutes after breakfast, lunch and dinner. After 30 days, how many hours does he spend brushing his teeth?"""
    # Define the number of days and the time spent brushing per day
    days = 30
    time_per_day = 6  # 2 minutes after breakfast, lunch, and dinner

    # Calculate the total time spent brushing over the 30-day period
    total_time = days * time_per_day

    # Convert the total time to hours
    hours = total_time / 60

    # Return the result
    result = hours
    return result

print(solution())