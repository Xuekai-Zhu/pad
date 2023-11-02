def solution():
    """Jack bought an ice cream cone before jogging to the beach. If the ice cream cone will melt in 10 minutes, the beach is 16 blocks away, and each block is 1/8th of a mile, how fast does Jack need to jog (in miles per hour) to get to the beach before the ice cream melts?"""
    ice_cream_time = 10 / 60  # convert to hours
    beach_distance = 16 * 1/8  # convert blocks to miles
    time_to_get_to_beach = beach_distance / jack_speed
    jack_speed = time_to_get_to_beach / ice_cream_time
    result = round(jack_speed, 2)
    return result

print(solution())