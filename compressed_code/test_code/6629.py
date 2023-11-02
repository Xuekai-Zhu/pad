def solution():
    
    width_tiles = 10
    length_tiles = 20
    tile_size_inches = 6
    square_footage = (width_tiles * tile_size_inches * length_tiles * tile_size_inches) / 144
    result = square_footage
    return result

print(solution())