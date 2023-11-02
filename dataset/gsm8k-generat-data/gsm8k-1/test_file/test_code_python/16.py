def solution():
    """I have 10 liters of orange drink that are two-thirds water and I wish to add it to 15 liters of pineapple drink that is three-fifths water. But as I pour it, I spill one liter of the orange drink. How much water is in the remaining 24 liters?"""
    orange_liters = 10 - 1
    orange_water = 2 / 3 * orange_liters
    pineapple_liters = 15
    pineapple_water = 3 / 5 * pineapple_liters
    total_liters = orange_liters + pineapple_liters
    total_water = orange_water + pineapple_water
    remaining_water = total_water / total_liters * 24
    result = remaining_water
    return result

print(solution())