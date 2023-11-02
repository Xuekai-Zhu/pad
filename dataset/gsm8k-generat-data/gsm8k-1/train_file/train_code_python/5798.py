def solution():
    """Trent walked 4 blocks from his house to the bus stop. He rode the bus 7 blocks to the library. Later, he came home the same way. How many blocks did Trent travel in all?"""
    blocks_to_bus_stop = 4
    blocks_to_library = 7
    total_blocks_travelled = (blocks_to_bus_stop + blocks_to_library) * 2
    result = total_blocks_travelled
    return result

print(solution())