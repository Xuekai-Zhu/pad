def solution():
    tile_size = 6
    kitchen_width = 48
    kitchen_length = 72
    num_tiles_width = kitchen_width / tile_size
    num_tiles_length = kitchen_length / tile_size
    total_tiles = num_tiles_width * num_tiles_length
    result = total_tiles
    return result

print(solution())