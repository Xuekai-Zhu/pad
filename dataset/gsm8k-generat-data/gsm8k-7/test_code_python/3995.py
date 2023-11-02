def solution():
    tile_size = 6 # in square inches
    kitchen_length = 48 # in inches
    kitchen_width = 72 # in inches

    # Calculate the area of the kitchen in square inches
    kitchen_area = kitchen_length * kitchen_width

    # Calculate the number of tiles needed
    num_tiles = kitchen_area / tile_size

    result = num_tiles
    return result

print(solution())