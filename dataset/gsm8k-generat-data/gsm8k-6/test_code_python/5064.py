def solution():
    # Calculate the total number of tiles needed
    total_square_feet = 10 * 25
    total_tiles = total_square_feet * 4

    # Calculate the number of green tiles needed and the cost
    green_tiles = total_tiles * 0.4
    green_cost = 3 * green_tiles

    # Calculate the number of red tiles needed and the cost
    red_tiles = total_tiles - green_tiles
    red_cost = 1.5 * red_tiles

    # Calculate the total cost of the tile
    total_cost = green_cost + red_cost
    result = total_cost
    return result

print(solution())