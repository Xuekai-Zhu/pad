def solution():
    """Annie walked 5 blocks from her house to the bus stop. She rode the bus 7 blocks to the coffee shop. Later, she came home the same way. How many blocks did Annie travel in all?"""
    walking_blocks = 5
    bus_blocks = 7
    total_blocks = walking_blocks + (bus_blocks * 2)
    result = total_blocks
    return result

print(solution())