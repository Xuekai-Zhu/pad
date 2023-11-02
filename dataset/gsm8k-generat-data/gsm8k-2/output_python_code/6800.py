def solution():
    """36 liters of diesel fuel is worth €18. The tank of this pickup truck can hold 64 liters. How much does a full tank of diesel fuel cost?"""
    price_per_liter = 18 / 36
    full_tank_price = price_per_liter * 64
    result = full_tank_price
    return result

print(solution())