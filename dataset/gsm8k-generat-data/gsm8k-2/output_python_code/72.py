def solution():
    """Nancy is filling an aquarium for her fish. She fills it halfway and goes to answer the door. While she's gone, her cat knocks the aquarium over and spills half the water in it. Then Nancy comes back and triples the amount of water in the aquarium. If the aquarium is 4 feet long, 6 feet wide, and 3 feet high, how many cubic feet of water are in the aquarium?"""
    length = 4
    width = 6
    height = 3
    half_volume = 0.5 * length * width * height
    remaining_volume = 0.5 * half_volume
    total_volume = half_volume + remaining_volume
    tripled_volume = 3 * total_volume
    result = tripled_volume
    return result

print(solution())