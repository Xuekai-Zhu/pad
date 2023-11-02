def solution():
    """36 liters of diesel fuel is worth €18. The tank of this pickup truck can hold 64 liters. How much does a full tank of diesel fuel cost?"""
    liters_per_price = 36/18
    price_per_liter = 1/liters_per_price
    full_tank_cost = price_per_liter * 64
    result = full_tank_cost
    return result

print(solution())