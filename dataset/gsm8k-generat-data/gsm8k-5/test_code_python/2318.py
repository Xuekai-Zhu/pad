def solution():
    short_hair_time = 10  # It takes 10 minutes to dry a short-haired dog
    full_hair_time = 2 * short_hair_time  # It takes twice as long to dry a full-haired dog
    num_short_hair_dogs = 6
    num_full_hair_dogs = 9

    # Calculate the total time to dry all short-haired dogs
    total_short_hair_time = short_hair_time * num_short_hair_dogs

    # Calculate the total time to dry all full-haired dogs
    total_full_hair_time = full_hair_time * num_full_hair_dogs

    # Calculate the total time to dry all dogs in minutes
    total_time_minutes = total_short_hair_time + total_full_hair_time

    # Convert total time to hours
    total_time_hours = total_time_minutes / 60
    result = total_time_hours
    return result

print(solution())