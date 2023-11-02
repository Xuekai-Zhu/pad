def solution():
    """A bathroom has 10 6 inch tiles along its width and 20 6 inch tiles along its length.  What is the square footage of the bathroom?"""
    # Calculate the total number of tiles
    total_tiles = 10 * 20

    # Convert the size of one tile from inches to feet
    tile_size_ft = 6/12

    # Calculate the area of one tile in sq ft
    tile_area_sqft = tile_size_ft ** 2

    # Calculate the total square footage of the bathroom
    bathroom_sqft = total_tiles * tile_area_sqft

    # Display the square footage
    result = bathroom_sqft
    return result

print(solution())