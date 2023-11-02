def solution():
    """Mary is building a mosaic for her school cafeteria's wall. It will be 10 feet tall and 15 feet long. Each tile she uses is 1 inch square. How many tiles will she need?"""
    wall_height = 10 * 12 # convert feet to inches
    wall_length = 15 * 12 # convert feet to inches
    tile_size = 1 # each tile is 1 inch square
    total_tiles = wall_height * wall_length / tile_size
    result = total_tiles
    return result

print(solution())