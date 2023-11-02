def solution():
    num_dancers = 8
    num_braids_per_dancer = 5
    braid_time_per_braid = 30  # seconds

    # Calculate the total number of braids that need to be done
    total_braids = num_dancers * num_braids_per_dancer

    # Calculate the total time it will take to braid all the hair in seconds
    total_time_in_seconds = total_braids * braid_time_per_braid

    # Convert the total time to minutes
    total_time_in_minutes = total_time_in_seconds / 60

    result = total_time_in_minutes
    return result

print(solution())