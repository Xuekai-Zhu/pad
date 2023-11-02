def solution():
    blocks_north = 3
    blocks_west = 7 * blocks_north
    blocks_south = 8
    blocks_east = 2 * blocks_west

    total_blocks = blocks_north + blocks_west + blocks_south + blocks_east

    time_in_minutes = total_blocks / 2
    result = time_in_minutes
    return result

print(solution())