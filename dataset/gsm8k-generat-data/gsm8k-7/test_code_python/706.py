def solution():
    blue_tiles = 48
    red_tiles = 32
    total_tiles = 100

    # Calculate the number of tiles needed to complete the pool
    tiles_needed = total_tiles - (blue_tiles + red_tiles)
    result = tiles_needed
    return result

print(solution())