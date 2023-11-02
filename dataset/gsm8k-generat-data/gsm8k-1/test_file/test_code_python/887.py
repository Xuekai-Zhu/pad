def solution():
    """A whirligig spins at five times the speed of a thingamabob. A whatchamacallit spins eleven times faster than a thingamabob. A whatchamacallit spins at 121 meters per second. How fast does a whirligig spin?"""
    thingamabob_speed = 121 / 11
    whirligig_speed = 5 * thingamabob_speed
    result = whirligig_speed
    return result

print(solution())