def solution():
    """Carson is going to spend 4 hours at a carnival. The wait for the roller coaster is 30 minutes, the wait for the tilt-a-whirl is 60 minutes, and the wait for the giant slide is 15 minutes. If Carson rides the roller coaster 4 times and the tilt-a-whirl once, how many times can he ride the giant slide? (Wait times include the time actually spent on the ride.)"""
    total_time = 4 * 60 # convert hours to minutes
    roller_coaster_time = 30 * 4 # 4 times on roller coaster
    tilt_a_whirl_time = 60
    total_time_spent = roller_coaster_time + tilt_a_whirl_time
    giant_slide_time = 15
    giant_slide_rides = (total_time - total_time_spent) // giant_slide_time
    result = giant_slide_rides
    return result

print(solution())