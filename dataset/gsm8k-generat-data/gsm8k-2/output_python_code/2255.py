def solution():
    """Carson is going to spend 4 hours at a carnival. The wait for the roller coaster is 30 minutes, the wait for the tilt-a-whirl is 60 minutes, and the wait for the giant slide is 15 minutes. If Carson rides the roller coaster 4 times and the tilt-a-whirl once, how many times can he ride the giant slide? (Wait times include the time actually spent on the ride.)"""
    total_time = 4 * 60  # in minutes

    roller_coaster_time = 4 * (30 + 2)  # 30 for wait time, 2 for actual ride time
    tilt_a_whirl_time = 60 + 3  # 60 for wait time, 3 for actual ride time

    # Remaining time for the giant slide
    remaining_time = total_time - roller_coaster_time - tilt_a_whirl_time

    giant_slide_time = 15 + 2  # 15 for wait time, 2 for actual ride time

    # Number of times Carson can ride the giant slide
    ride_count = remaining_time // giant_slide_time

    result = ride_count
    return result

print(solution())