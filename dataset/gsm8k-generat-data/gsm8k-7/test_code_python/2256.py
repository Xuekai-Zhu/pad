def solution():
    carnival_time = 4 * 60  # convert to minutes
    roller_coaster_time = 30 * 4  # 4 rides on roller coaster
    tilt_a_whirl_time = 60
    giant_slide_time = 15

    # Calculate the total time spent on roller coaster and tilt-a-whirl
    total_time_spent = roller_coaster_time + tilt_a_whirl_time

    # Calculate the remaining time for giant slide
    remaining_time = carnival_time - total_time_spent

    # Calculate the number of rides on giant slide
    num_giant_slide_rides = remaining_time // giant_slide_time
    result = num_giant_slide_rides
    return result

print(solution())