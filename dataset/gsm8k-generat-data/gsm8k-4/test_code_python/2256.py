def solution():
    """Carson is going to spend 4 hours at a carnival. The wait for the roller coaster is 30 minutes, the wait for the tilt-a-whirl is 60 minutes, and the wait for the giant slide is 15 minutes. If Carson rides the roller coaster 4 times and the tilt-a-whirl once, how many times can he ride the giant slide? (Wait times include the time actually spent on the ride.)"""
    # Define the total time Carson has at the carnival
    total_time = 4 * 60 # in minutes

    # Define the time it takes for each ride
    roller_coaster_time = 30
    tilt_a_whirl_time = 60
    giant_slide_time = 15

    # Define the number of times Carson rides the roller coaster and tilt-a-whirl
    roller_coaster_rides = 4
    tilt_a_whirl_rides = 1

    # Calculate the total time spent on the roller coaster and tilt-a-whirl
    roller_coaster_total_time = roller_coaster_rides * roller_coaster_time
    tilt_a_whirl_total_time = tilt_a_whirl_rides * tilt_a_whirl_time

    # Calculate the remaining time for riding the giant slide
    remaining_time = total_time - roller_coaster_total_time - tilt_a_whirl_total_time

    # Calculate the number of times Carson can ride the giant slide
    giant_slide_rides = remaining_time // giant_slide_time

    result = giant_slide_rides
    return result

print(solution())