def solution():
    # Calculate the total time, in minutes, to dry all the dogs
    time_for_short_hair = 10  # minutes to dry one short-haired dog
    time_for_full_hair = 2 * time_for_short_hair  # minutes to dry one full-haired dog
    total_time = (time_for_short_hair * 6) + (time_for_full_hair * 9)  # total minutes to dry all dogs

    # Convert the total time to hours
    hours = total_time / 60

    result = hours
    return result

print(solution())