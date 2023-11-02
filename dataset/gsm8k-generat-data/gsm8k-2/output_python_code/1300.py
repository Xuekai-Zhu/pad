def solution():
    """Each wall of a 3 sided shower has 8 tiles running the width of the wall and 20 tiles running the height of the wall. How many tiles are in the shower?"""
    width_tiles = 8
    height_tiles = 20
    wall_area = width_tiles * height_tiles
    shower_area = wall_area * 3
    result = shower_area
    return result

print(solution())