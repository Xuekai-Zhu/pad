def solution():
    ice_cream_melt_time = 10 # in minutes
    distance_to_beach_blocks = 16
    distance_to_beach_miles = distance_to_beach_blocks * 1/8 # 1 block is 1/8th of a mile
    time_to_get_to_beach = distance_to_beach_miles * 60 # convert to minutes
    speed_required = distance_to_beach_miles / (ice_cream_melt_time/60)
    result = speed_required
    return result

print(solution())