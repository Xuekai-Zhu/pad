def solution():
    num_tiles_width = 8
    num_tiles_height = 20
    num_walls = 3

    # Calculate the total number of tiles on one wall
    tiles_per_wall = num_tiles_width * num_tiles_height

    # Calculate the total number of tiles for all walls
    total_tiles = tiles_per_wall * num_walls
    result = total_tiles
    return result

print(solution())