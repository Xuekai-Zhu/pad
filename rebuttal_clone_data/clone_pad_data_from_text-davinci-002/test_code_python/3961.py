def solution():
    blocks_north = 3
    blocks_west = blocks_north * 7
    blocks_south = 8
    blocks_east = blocks_south * 2
    blocks_total = blocks_north + blocks_west + blocks_south + blocks_east
    time = blocks_total / 2
    result = time
    return result

print(solution())