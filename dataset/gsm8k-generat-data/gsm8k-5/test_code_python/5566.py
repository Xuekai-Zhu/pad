def solution():
    blocks_to_bus_stop = 5  # Annie walked 5 blocks to the bus stop
    blocks_on_bus = 7  # Annie rode the bus for 7 blocks
    total_blocks = 2 * (blocks_to_bus_stop + blocks_on_bus)  # Annie came back the same way, so we double the distance
    result = total_blocks
    return result

print(solution())