def solution():
    """Trent walked 4 blocks from his house to the bus stop. He rode the bus 7 blocks to the library. Later, he came home the same way. How many blocks did Trent travel in all?"""
    # Define the distance Trent walked and rode the bus
    walking_distance = 4
    bus_distance = 7

    # Calculate the total distance Trent traveled
    total_distance = 2 * (walking_distance + bus_distance)

    # return the result
    result = total_distance
    return result

print(solution())