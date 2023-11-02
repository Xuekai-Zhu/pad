def solution():
    
    total_tiles = 20
    yellow_tiles = 3
    blue_tiles = yellow_tiles + 1
    purple_tiles = 6
    white_tiles = total_tiles - yellow_tiles - blue_tiles - purple_tiles
    result = white_tiles
    return result

print(solution())