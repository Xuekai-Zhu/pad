def solution():
    bridge_length = 1.1 # in miles
    drone_speed = 179.6 # in MPH
    drone_speed_miles_per_min = drone_speed / 60 # convert MPH to miles per minute
    drone_distance_per_min = 3 # in miles
    time_to_cross_bridge = bridge_length / drone_speed_miles_per_min # in minutes
    if time_to_cross_bridge <= (18/60): # convert 18 seconds to minutes
        result = "yes"
    else:
        result = "no"
    return result

print(solution())