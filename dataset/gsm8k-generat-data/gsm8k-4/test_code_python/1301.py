def solution():
    """Each wall of a 3 sided shower has 8 tiles running the width of the wall and 20 tiles running the height of the wall. How many tiles are in the shower?"""
    # Define the number of tiles running the width and height of each wall
    width_tiles = 8
    height_tiles = 20

    # Calculate the number of tiles on each wall
    wall_tiles = width_tiles * height_tiles

    # Calculate the total number of tiles in the shower
    shower_tiles = wall_tiles * 3

    # return the result
    result = shower_tiles
    return result

print(solution())