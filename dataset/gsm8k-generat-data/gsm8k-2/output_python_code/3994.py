def solution():
    """Kimiko is retiling her kitchen floor. Each tile is 6 square inches. If her kitchen is 48 inches by 72 inches, how many tiles does Kimiko need to buy?"""
    kitchen_area = 48 * 72
    tile_area = 6
    num_tiles = kitchen_area / tile_area
    result = num_tiles
    return result

print(solution())