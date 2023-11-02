def solution():
    # Convert the total time to minutes
    total_time_minutes = 3 * 60 + 36

    # Calculate the time per mile in minutes
    time_per_mile_minutes = total_time_minutes / 24

    result = time_per_mile_minutes
    return result

print(solution())