def solution():
    total_time = 7.5 * 60  # Adah practiced for 7.5 hours, so convert to minutes
    time_per_day = 86 * 2  # Adah practiced for 86 minutes on each of 2 days

    # Calculate the total time Adah practiced on the other days
    other_time = total_time - time_per_day
    result = other_time
    return result

print(solution())