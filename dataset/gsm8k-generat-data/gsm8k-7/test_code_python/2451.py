def solution():
    towels_per_wash = 7
    wash_time = 1 #in hours
    available_time = 2 #in hours
    total_towels = 98

    # Calculate the number of washes needed to wash all the towels
    num_washes = total_towels // towels_per_wash
    if total_towels % towels_per_wash != 0:
        num_washes += 1

    # Calculate the total time needed to wash all the towels
    total_time = num_washes * wash_time

    # Calculate the number of days needed to wash all the towels
    num_days = total_time // available_time
    if total_time % available_time != 0:
        num_days += 1

    result = num_days
    return result

print(solution())