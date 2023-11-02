def solution():
    """Rodney and Todd are rowing down a river that is 50 yards wide at one end. If the river's width increases from this end uniformly by 2 yards every 10 meters along, and they row along the river at a rate of 5 m/s, how long (in seconds) will it take them to get to the point where the river is 80 yards wide?"""
    width_start = 50
    width_end = 80
    rate = 5 # in m/s
    width_change_per_meter = 2/10 # in yards/meter
    distance_to_cover = (width_end - width_start) / width_change_per_meter
    time_taken = distance_to_cover / (rate * 1.09361) # converting yards to meters
    result = time_taken
    
    return result

print(solution())