def solution():
    # Convert wait times to hours
    roller_coaster_wait = 0.5
    tilt_a_whirl_wait = 1
    giant_slide_wait = 0.25

    # Calculate time spent on roller coaster and tilt-a-whirl
    roller_coaster_time = 4 * roller_coaster_wait
    tilt_a_whirl_time = tilt_a_whirl_wait

    # Calculate total time already spent and remaining time
    total_time_spent = roller_coaster_time + tilt_a_whirl_time
    remaining_time = 4 - total_time_spent

    # Calculate number of times Carson can ride the giant slide
    giant_slide_rides = remaining_time / giant_slide_wait
    result = int(giant_slide_rides)
    return result

print(solution())