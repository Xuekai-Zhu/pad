def solution():
    """June made a design with 20 equal tiles. Three tiles are yellow and the number of blue tiles is one more than the number of yellow tiles. Six tiles are purple and the remaining tiles are white. How many white tiles are there?"""
    # Define the total number of tiles
    total_tiles = 20

    # Define the number of yellow tiles
    yellow_tiles = 3

    # Define the number of blue tiles, which is one more than the number of yellow tiles
    blue_tiles = yellow_tiles + 1

    # Define the number of purple tiles
    purple_tiles = 6

    # Calculate the number of white tiles
    white_tiles = total_tiles - yellow_tiles - blue_tiles - purple_tiles

    # return the result
    result = white_tiles
    return result

print(solution())