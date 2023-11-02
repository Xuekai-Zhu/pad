def solution():
    # Calculate the total square footage of the courtyard
    square_footage = 10 * 25

    # Calculate the total number of tiles needed, assuming 4 tiles per square foot
    total_tiles = square_footage * 4

    # Calculate the number of green tiles needed, assuming 40% of total tiles
    green_tiles = total_tiles * 0.4

    # Calculate the number of red tiles needed
    red_tiles = total_tiles - green_tiles

    # Calculate the cost of the green tiles
    green_cost = green_tiles * 3

    # Calculate the cost of the red tiles
    red_cost = red_tiles * 1.5

    # Calculate the total cost of the tiles
    total_cost = green_cost + red_cost
    result = total_cost
    return result

print(solution())