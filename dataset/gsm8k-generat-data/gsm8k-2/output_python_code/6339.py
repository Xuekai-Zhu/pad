def solution():
    """Blake wants to spend his Friday making milkshakes for his family. He knows that he needs 4 ounces of milk and 12 ounces of ice cream for each milkshake. If he has 72 ounces of milk and 192 ounces of ice cream, how much milk will be left over when he is done?"""
    milk_per_milkshake = 4
    ice_cream_per_milkshake = 12
    total_milkshakes = min(72 // milk_per_milkshake, 192 // ice_cream_per_milkshake)
    total_milk_used = total_milkshakes * milk_per_milkshake
    milk_leftover = 72 - total_milk_used
    result = milk_leftover
    return result

print(solution())