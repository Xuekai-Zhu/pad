def solution():
    
    height_in_inches = 10 * 12
    length_in_inches = 15 * 12
    tile_area_in_inches = 1 * 1
    total_area_in_inches = height_in_inches * length_in_inches
    tiles_needed = total_area_in_inches / tile_area_in_inches
    result = tiles_needed
    return result

print(solution())