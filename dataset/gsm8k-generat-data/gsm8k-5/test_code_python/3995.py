def solution():
    kitchen_area = 48 * 72  # Kimiko's kitchen area in square inches
    tile_area = 6  # Each tile covers 6 square inches

    # Calculate the number of tiles needed to cover the kitchen floor
    num_tiles = kitchen_area / tile_area
    result = num_tiles
    return result

print(solution())