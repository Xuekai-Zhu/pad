def solution():
    """The Zargon Destroyer spacecraft can travel at 2 billion miles per hour in normal space, but when moving through a black hole they travel three times faster. If the Zargon Destroyer is making a voyage that travels seven hours in normal space and two hours through a black hole, how many billions of miles would they have traveled?"""
    normal_speed = 2
    black_hole_speed = 3 * normal_speed
    normal_distance = normal_speed * 7
    black_hole_distance = black_hole_speed * 2
    total_distance = normal_distance + black_hole_distance
    result = total_distance / 1e9
    return result

print(solution())