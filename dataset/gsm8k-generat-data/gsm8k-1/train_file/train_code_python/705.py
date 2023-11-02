def solution():
    """A pool has 48 blue tiles and 32 red tiles. If the pool needs 100 tiles to be completed, how many more tiles are needed?"""
    blue_tiles = 48
    red_tiles = 32
    total_tiles = 100
    tiles_needed = total_tiles - (blue_tiles + red_tiles)
    result = tiles_needed
    return result

print(solution())