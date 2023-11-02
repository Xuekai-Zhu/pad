def solution():
    
    wall_height = 10 * 12 
    wall_length = 15 * 12 
    tile_size = 1 
    total_tiles = wall_height * wall_length / tile_size
    result = total_tiles
    return result

print(solution())