def solution():
    # Define the time to dry a short-haired dog and a full-haired dog
    time_short_haired = 10
    time_full_haired = 2 * time_short_haired

    # Calculate the total time to dry all the short-haired dogs
    total_time_short_haired = time_short_haired * 6

    # Calculate the total time to dry all the full-haired dogs
    total_time_full_haired = time_full_haired * 9

    # Calculate the total time to dry all dogs in minutes
    total_time_minutes = total_time_short_haired + total_time_full_haired

    # Convert the total time to hours
    total_time_hours = total_time_minutes / 60

    result = total_time_hours
    return result

print(solution())