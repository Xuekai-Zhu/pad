def solution():
    """Claudia has 122 ounces of water and is filling up cups. She has 8-ounce glasses, 5-ounce glasses, and 4-ounce glasses.
    If she fills six 5 ounce glasses and four 8 ounce glasses, how many 4 ounce glasses can she fill with the remaining water?"""
    water_amount = 122
    total_filled = 6 * 5 + 4 * 8
    remaining_water = water_amount - total_filled
    four_oz_glasses = remaining_water // 4
    result = four_oz_glasses
    return result

print(solution())