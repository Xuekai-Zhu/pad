def solution():
 
    width_tiles = 10
    length_tiles = 20
    tile_sq_inch = 6
    tile_sq_foot = tile_sq_inch / 12
    bathroom_square_footage = width_tiles * tile_sq_foot * length_tiles * tile_sq_foot
    result = bathroom_square_footage
    return result

print(solution())