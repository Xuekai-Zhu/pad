def solution():
    height_ft = 10
    length_ft = 15
    tile_size_in = 1

    # Convert feet to inches
    height_in = height_ft * 12
    length_in = length_ft * 12

    # Calculate the total number of tiles needed
    num_tiles = (height_in * length_in) / (tile_size_in ** 2)
    result = num_tiles
    return result

print(solution())