def solution():
    total_tiles = 20  # June made a design with 20 equal tiles
    yellow_tiles = 3  # Three tiles are yellow
    blue_tiles = yellow_tiles + 1  # The number of blue tiles is one more than the number of yellow tiles
    purple_tiles = 6  # Six tiles are purple

    # Calculate the number of white tiles
    white_tiles = total_tiles - yellow_tiles - blue_tiles - purple_tiles
    result = white_tiles
    return result

print(solution())