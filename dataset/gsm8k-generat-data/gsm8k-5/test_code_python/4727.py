def solution():
    start_time = 6*60  # Convert start time to minutes
    time_elapsed = 10  # 10 minutes past 6
    days_elapsed = 40  # 40 days have passed since March 1st
    increment = 1.2  # The sun sets 1.2 minutes later each day

    total_time_elapsed = days_elapsed * increment  # Find total time elapsed in minutes
    current_time = start_time + time_elapsed + total_time_elapsed  # Find current time in minutes
    sunset_time = start_time + (increment * days_elapsed)  # Find sunset time on current day in minutes

    # Calculate how many minutes remain until sunset
    time_remaining = sunset_time - current_time
    result = time_remaining
    return result

print(solution())