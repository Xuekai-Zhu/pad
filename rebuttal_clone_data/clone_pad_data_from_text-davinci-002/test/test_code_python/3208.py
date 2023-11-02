def solution():
    tiles_don = 3
    tiles_ken = tiles_don + 2
    tiles_laura = tiles_ken * 2
    tiles_kim = tiles_laura - 3
    minutes = 15
    total_tiles = (tiles_don * minutes) + (tiles_ken * minutes) + (tiles_laura * minutes) + (tiles_kim * minutes)
    result = total_tiles
    return result

print(solution())