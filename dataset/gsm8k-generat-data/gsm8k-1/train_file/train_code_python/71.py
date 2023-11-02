def solution():
    """Nancy is filling an aquarium for her fish. She fills it halfway and goes to answer the door. While she's gone, her cat knocks the aquarium over and spills half the water in it. Then Nancy comes back and triples the amount of water in the aquarium. If the aquarium is 4 feet long, 6 feet wide, and 3 feet high, how many cubic feet of water are in the aquarium?"""
    length = 4
    width = 6
    height = 3
    total_volume = length * width * height
    half_full_volume = total_volume / 2
    spilled_volume = half_full_volume / 2
    new_volume = half_full_volume + spilled_volume + (3 * half_full_volume)
    result = new_volume
    return result

print(solution())