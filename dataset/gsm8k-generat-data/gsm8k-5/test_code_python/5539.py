def solution():
    # Calculate the total time Monica spent studying on Wednesday and Thursday
    time_wednesday = 2
    time_thursday = 3 * time_wednesday

    # Calculate the time Monica spent studying on Friday
    time_friday = 0.5 * time_thursday

    # Calculate the total time Monica spent studying on the first four days
    total_time_first_four_days = time_wednesday + time_thursday + time_friday

    # Calculate the total time Monica spent studying during the weekend
    time_weekend = 2 * (time_wednesday + time_thursday + time_friday)

    # Calculate the total time Monica spent studying during the five days
    total_time = total_time_first_four_days + time_weekend
    result = total_time
    return result

print(solution())