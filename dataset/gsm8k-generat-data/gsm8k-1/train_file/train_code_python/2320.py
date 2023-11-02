def solution():
    """Pete walked 5 blocks from his house to the bus garage in Houston. He rode the bus 20 blocks to the post office to get some stamps. Later, he came home the same way. How many blocks did Pete travel in all?"""
    walking_blocks = 5
    bus_blocks = 20
    total_blocks = 2 * (walking_blocks + bus_blocks)
    result = total_blocks
    return result

print(solution())