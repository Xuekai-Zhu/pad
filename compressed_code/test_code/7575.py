def solution():
    
    total_time = 4 * 60 
    roller_coaster_time = 30 * 4 
    tilt_a_whirl_time = 60
    total_time_spent = roller_coaster_time + tilt_a_whirl_time
    giant_slide_time = 15
    giant_slide_rides = (total_time - total_time_spent) // giant_slide_time
    result = giant_slide_rides
    return result

print(solution())