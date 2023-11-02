def solution():
    tiles_per_width = 8  # Each wall has 8 tiles running the width
    tiles_per_height = 20  # Each wall has 20 tiles running the height
    num_walls = 3  # There are 3 walls in the shower

    # Calculate the total number of tiles
    total_tiles = tiles_per_width * tiles_per_height * num_walls
    result = total_tiles
    return result

print(solution())