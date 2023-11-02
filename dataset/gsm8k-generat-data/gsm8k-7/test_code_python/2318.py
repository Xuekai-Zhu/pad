def solution():
    time_per_short_hair = 10  # minutes
    time_per_full_hair = 2 * time_per_short_hair  # minutes
    num_short_hair = 6
    num_full_hair = 9

    # Calculate the total time needed to dry all short-haired dogs
    total_time_short_hair = num_short_hair * time_per_short_hair

    # Calculate the total time needed to dry all full-haired dogs
    total_time_full_hair = num_full_hair * time_per_full_hair

    # Calculate the total time needed to dry all dogs
    total_time = (total_time_short_hair + total_time_full_hair) / 60  # hours
    result = total_time
    return result

print(solution())