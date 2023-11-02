def solution():
    # Calculate the total time Joan spent on breaks
    total_break_time = (30 + 2*15) / 60  # lunch break + 2 bathroom breaks, converted to hours
    
    # Calculate the driving time
    driving_distance = 480  # miles
    driving_speed = 60  # mph
    driving_time = driving_distance / driving_speed
    
    # Calculate the total time for the trip
    total_time = driving_time + total_break_time
    
    result = total_time
    return result

print(solution())