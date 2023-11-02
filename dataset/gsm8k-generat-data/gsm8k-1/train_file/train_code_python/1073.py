def solution():
    """A bathroom has 10 6 inch tiles along its width and 20 6 inch tiles along its length. What is the square footage of the bathroom?"""
    width_tiles = 10
    length_tiles = 20
    tile_size_inches = 6
    square_footage = (width_tiles * tile_size_inches * length_tiles * tile_size_inches) / 144
    result = square_footage
    return result

print(solution())