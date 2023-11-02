def solution():
    # Calculate total practice time on weekdays
    weekday_time = 30 * 5

    # Calculate practice time on Saturday
    saturday_time = 30 * 3

    # Calculate total practice time for the week
    total_time = weekday_time + saturday_time

    # Convert total time to hours
    hours = total_time / 60
    result = hours
    return result

print(solution())