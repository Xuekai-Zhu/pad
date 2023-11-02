def solution():
    """Nancy is filling an aquarium for her fish. She fills it halfway and goes to answer the door. While she's gone, her cat knocks the aquarium over and spills half the water in it. Then Nancy comes back and triples the amount of water in the aquarium. If the aquarium is 4 feet long, 6 feet wide, and 3 feet high, how many cubic feet of water are in the aquarium?"""
    # Calculate the volume of the aquarium
    aquarium_volume = 4 * 6 * 3

    # Fill the aquarium halfway
    water_volume = aquarium_volume / 2

    # Knock over the aquarium and spill half the water
    water_volume /= 2

    # Triple the amount of remaining water
    water_volume *= 3

    result = water_volume
    return result

print(solution())