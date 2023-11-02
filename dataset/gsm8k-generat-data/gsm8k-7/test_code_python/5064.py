def solution():
    courtyard_area = 10 * 25  # square feet
    tiles_per_square_foot = 4
    total_tiles = courtyard_area * tiles_per_square_foot

    green_percentage = 0.4
    green_tiles = int(green_percentage * total_tiles)
    red_tiles = total_tiles - green_tiles

    green_tile_cost = 3
    red_tile_cost = 1.5

    total_cost = (green_tiles * green_tile_cost) + (red_tiles * red_tile_cost)
    result = total_cost
    return result

print(solution())