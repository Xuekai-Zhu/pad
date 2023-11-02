def solution():
    """Kimiko is retiling her kitchen floor. Each tile is 6 square inches. If her kitchen is 48 inches by 72 inches, how many tiles does Kimiko need to buy?"""
    tile_area = 6 # in square inches
    kitchen_area = 48 * 72 # in square inches
    tiles_needed = kitchen_area / tile_area
    result = tiles_needed
    return result

print(solution())