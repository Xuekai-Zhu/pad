def solution():
    # Calculate the total number of braids to be done
    total_braids = 8 * 5

    # Calculate the total time it will take to braid all the hair in seconds
    total_time_seconds = total_braids * 30

    # Convert the total time to minutes
    total_time_minutes = total_time_seconds / 60

    result = total_time_minutes
    return result

print(solution())