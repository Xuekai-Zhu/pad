def solution():
    """The Zargon Destroyer spacecraft can travel at 2 billion miles per hour in normal space, but when moving through a black hole they travel three times faster. If the Zargon Destroyer is making a voyage that travels seven hours in normal space and two hours through a black hole, how many billions of miles would they have traveled?"""
    normal_speed = 2 # billion miles per hour
    black_hole_speed = 3 * normal_speed # billion miles per hour
    normal_time = 7 # hours
    black_hole_time = 2 # hours
    normal_distance = normal_speed * normal_time # billion miles
    black_hole_distance = black_hole_speed * black_hole_time # billion miles
    total_distance = normal_distance + black_hole_distance # billion miles
    result = total_distance
    return result

print(solution())