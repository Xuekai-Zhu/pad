def solution():
    """Blake wants to spend his Friday making milkshakes for his family. He knows that he needs 4 ounces of milk and 12 ounces of ice cream for each milkshake. If he has 72 ounces of milk and 192 ounces of ice cream, how much milk will be left over when he is done?"""
    milk_per_shake = 4
    ice_cream_per_shake = 12
    total_shakes = min(72/milk_per_shake, 192/ice_cream_per_shake)
    total_milk_needed = total_shakes * milk_per_shake
    milk_leftover = 72 - total_milk_needed
    result = milk_leftover
    return result

print(solution())