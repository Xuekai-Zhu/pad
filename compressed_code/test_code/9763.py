def solution():
    
    width = 10
    length = 25
    area = width * length
    tiles_per_sqft = 4
    total_tiles_needed = area * tiles_per_sqft
    green_tiles_percent = 40
    green_tiles_needed = int(total_tiles_needed * (green_tiles_percent / 100))
    red_tiles_needed = total_tiles_needed - green_tiles_needed
    green_tile_cost = 3
    red_tile_cost = 1.5
    total_cost = (green_tiles_needed * green_tile_cost) + (red_tiles_needed * red_tile_cost)
    result = total_cost
    return result

print(solution())