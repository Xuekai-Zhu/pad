def solution():
    total_tiles = 20
    yellow_tiles = 3
    blue_tiles = yellow_tiles + 1
    purple_tiles = 6

    # Calculate the total number of non-white tiles
    non_white_tiles = yellow_tiles + blue_tiles + purple_tiles

    # Calculate the number of white tiles
    white_tiles = total_tiles - non_white_tiles
    result = white_tiles
    return result

print(solution())