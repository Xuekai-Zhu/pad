def solution():
    """June made a design with 20 equal tiles. Three tiles are yellow and the number of blue tiles is one more than the number of yellow tiles. Six tiles are purple and the remaining tiles are white. How many white tiles are there?"""
    # Define the number of yellow tiles and calculate the number of blue tiles
    yellow_tiles = 3
    blue_tiles = yellow_tiles + 1

    # Calculate the total number of colored tiles
    colored_tiles = yellow_tiles + blue_tiles + 6

    # Calculate the number of white tiles
    white_tiles = 20 - colored_tiles

    # Display the number of white tiles
    result = white_tiles
    return result

print(solution())