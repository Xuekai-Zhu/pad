def solution():
    mosaic_tiles_per_sqft = 24
    total_sqft = 36

    # Calculate the total number of mosaic tiles needed
    total_tiles = total_sqft * mosaic_tiles_per_sqft

    # Calculate the number of tiles needed for two thirds of the bathroom
    num_tiles_two_thirds = total_tiles * (2/3)

    result = num_tiles_two_thirds
    return result

print(solution())