def solution():
    # Define the number of yellow and blue tiles
    yellow_tiles = 3
    blue_tiles = yellow_tiles + 1

    # Define the number of purple tiles
    purple_tiles = 6

    # Calculate the total number of tiles
    total_tiles = yellow_tiles + blue_tiles + purple_tiles

    # Calculate the number of white tiles
    white_tiles = 20 - total_tiles
    result = white_tiles
    return result

print(solution())