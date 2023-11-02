def solution():
    """Mary is building a mosaic for her school cafeteria's wall. It will be 10 feet tall and 15 feet long. Each tile she uses is 1 inch square. How many tiles will she need?"""
    height_in_inches = 10 * 12
    length_in_inches = 15 * 12
    tile_area_in_inches = 1 * 1
    total_area_in_inches = height_in_inches * length_in_inches
    tiles_needed = total_area_in_inches / tile_area_in_inches
    result = tiles_needed
    return result

print(solution())