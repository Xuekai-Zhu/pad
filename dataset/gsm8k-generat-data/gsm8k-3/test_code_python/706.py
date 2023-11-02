def solution():
    """A pool has 48 blue tiles and 32 red tiles. If the pool needs 100 tiles to be completed, how many more tiles are needed?"""
    # Define the number of blue and red tiles
    blue_tiles = 48
    red_tiles = 32

    # Calculate the total number of tiles needed
    total_tiles = 100

    # Calculate the number of tiles needed to complete the pool
    needed_tiles = total_tiles - (blue_tiles + red_tiles)

    # Display the number of tiles needed
    result = needed_tiles
    return result

print(solution())