def solution():
    """Annie walked 5 blocks from her house to the bus stop. She rode the bus 7 blocks to the coffee shop. Later, she came home the same way. How many blocks did Annie travel in all?"""
    blocks_to_bus_stop = 5
    blocks_on_bus = 7
    total_blocks = (blocks_to_bus_stop + blocks_on_bus) * 2
    result = total_blocks
    return result

print(solution())