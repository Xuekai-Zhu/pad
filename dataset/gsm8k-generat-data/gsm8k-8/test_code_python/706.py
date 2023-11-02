def solution():
    # Calculate the total number of tiles already available
    total_tiles = 48 + 32

    # Calculate the number of tiles needed to complete the pool
    needed_tiles = 100 - total_tiles

    result = needed_tiles
    return result

print(solution())