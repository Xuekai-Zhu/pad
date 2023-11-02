def solution():
    
    courtyard_area = 10 * 25
    tile_needed = courtyard_area * 4
    green_tiles = tile_needed * 0.4
    red_tiles = tile_needed - green_tiles
    green_cost = green_tiles * 3
    red_cost = red_tiles * 1.5
    total_cost = green_cost + red_cost
    result = total_cost
    return result

print(solution())