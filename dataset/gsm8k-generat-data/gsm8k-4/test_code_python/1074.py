def solution():
    """A bathroom has 10 6 inch tiles along its width and 20 6 inch tiles along its length. What is the square footage of the bathroom?"""
    # Define the number of tiles along the width and length of the bathroom
    width_tiles = 10
    length_tiles = 20

    # Define the size of each tile in inches
    tile_size = 6

    # Calculate the total area of the bathroom in square inches
    area_inches = width_tiles * length_tiles * tile_size ** 2

    # Convert the area to square feet
    area_feet = area_inches / 144

    result = area_feet
    return result

print(solution())