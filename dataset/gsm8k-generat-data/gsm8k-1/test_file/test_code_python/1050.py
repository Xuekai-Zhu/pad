def solution():
    """My kitchen floor has a total area of 200 SqFt. I want to install new square floor tiles that cost $12 each,
    and each tile side is 1ft in length. How much will it cost me to renovate my kitchen floor?"""
    floor_area = 200
    tile_side_length = 1
    tile_cost = 12
    tiles_needed = floor_area / (tile_side_length ** 2)
    total_cost = tiles_needed * tile_cost
    result = total_cost
    return result

print(solution())