def solution():
    """A pool has 48 blue tiles and 32 red tiles. If the pool needs 100 tiles to be completed, how many more tiles are needed?"""
    # Define the number of blue tiles and red tiles
    blue_tiles = 48
    red_tiles = 32

    # Define the total number of tiles needed
    total_tiles_needed = 100

    # Calculate the number of tiles already available
    tiles_available = blue_tiles + red_tiles

    # Calculate the number of tiles needed to complete the pool
    tiles_needed = total_tiles_needed - tiles_available

    result = tiles_needed
    return result

print(solution())