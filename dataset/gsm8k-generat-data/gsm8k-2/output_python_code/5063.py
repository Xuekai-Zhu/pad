def solution():
    """Jackson is laying tile in a courtyard that measures 10 feet by 25 feet. He needs 4 tiles per square foot of space. 40% of the tiles are green marble that costs $3/tile, and the rest are red tile that costs $1.50/tile. How much does he pay total for tile?"""
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