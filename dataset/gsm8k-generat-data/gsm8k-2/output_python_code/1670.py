def solution():
    """Rodney and Todd are rowing down a river that is 50 yards wide at one end. If the river's width increases from this end uniformly by 2 yards every 10 meters along, and they row along the river at a rate of 5 m/s, how long (in seconds) will it take them to get to the point where the river is 80 yards wide?"""
    initial_width = 50
    final_width = 80
    width_increase_per_meter = 0.2
    distance_to_cover = (final_width - initial_width) / width_increase_per_meter
    time_taken = distance_to_cover / 5
    result = time_taken
    return result

print(solution())