def solution():
    # Calculate total jogging time in minutes for the weekdays
    weekdays_time = 4 * 30

    # Add extra jogging time on Tuesday and Friday
    total_time = weekdays_time + 35 + 55

    # Convert total jogging time to hours
    hours = total_time / 60
    result = hours
    return result

print(solution())