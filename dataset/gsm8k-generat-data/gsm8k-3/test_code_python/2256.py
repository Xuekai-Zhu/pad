def solution():
    """Carson is going to spend 4 hours at a carnival. The wait for the roller coaster is 30 minutes, the wait for the tilt-a-whirl is 60 minutes, and the wait for the giant slide is 15 minutes. If Carson rides the roller coaster 4 times and the tilt-a-whirl once,
    how many times can he ride the giant slide? (Wait times include the time actually spent on the ride.)"""
    # Define the wait time for each ride
    ROLLERCOASTER_WAIT = 30
    TILTAWHIRL_WAIT = 60
    GIANTSLIDE_WAIT = 15

    # Define the ride time for each ride
    ROLLERCOASTER_RIDE = 2
    TILTAWHIRL_RIDE = 3
    GIANTSLIDE_RIDE = 1

    # Define the total time spent on rides
    total_ride_time = 4 * 60 - (ROLLERCOASTER_WAIT * 4) - TILTAWHIRL_WAIT - GIANTSLIDE_WAIT

    # Calculate how many times Carson can ride the giant slide
    giant_slide_rides = total_ride_time // (GIANTSLIDE_RIDE + GIANTSLIDE_WAIT)

    # Display the number of giant slide rides Carson can take
    result = giant_slide_rides
    return result

print(solution())