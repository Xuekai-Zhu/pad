def solution():
    """June made a design with 20 equal tiles. Three tiles are yellow and the number of blue tiles is one more than the number of yellow tiles. Six tiles are purple and the remaining tiles are white. How many white tiles are there?"""
    total_tiles = 20
    yellow_tiles = 3
    blue_tiles = yellow_tiles + 1
    purple_tiles = 6
    white_tiles = total_tiles - yellow_tiles - blue_tiles - purple_tiles
    result = white_tiles
    
    return result

print(solution())