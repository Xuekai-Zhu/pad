def solution():
    """Trent walked 4 blocks from his house to the bus stop. He rode the bus 7 blocks to the library. Later, he came home the same way. How many blocks did Trent travel in all?"""
    walking_distance = 4
    bus_distance = 7
    total_distance = walking_distance + (2 * bus_distance)
    result = total_distance
    return result

print(solution())