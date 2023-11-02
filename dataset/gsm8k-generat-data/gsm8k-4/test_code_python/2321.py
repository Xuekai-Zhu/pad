def solution():
    """Pete walked 5 blocks from his house to the bus garage in Houston. He rode the bus 20 blocks to the post office to get some stamps. Later, he came home the same way. How many blocks did Pete travel in all?"""
    # Define the distance Pete walked, rode the bus, and the round trip
    walking_distance = 5
    bus_distance = 20
    round_trip = (walking_distance + bus_distance) * 2

    # Calculate the total distance Pete traveled
    total_distance = walking_distance + bus_distance + round_trip

    # Return the result
    result = total_distance
    return result

print(solution())