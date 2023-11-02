def solution():
    """Each wall of a 3 sided shower has 8 tiles running the width of the wall and 20 tiles running the height of the wall. How many tiles are in the shower?"""
    tiles_per_width = 8
    tiles_per_height = 20
    walls = 3
    total_tiles = tiles_per_width * tiles_per_height * walls
    result = total_tiles
    return result

print(solution())