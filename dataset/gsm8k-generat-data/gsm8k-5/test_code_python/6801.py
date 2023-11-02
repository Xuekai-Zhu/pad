def solution():
    fuel_price_per_liter = 18 / 36  # €18 for 36 liters of diesel fuel
    tank_capacity = 64  # The tank of the pickup truck can hold 64 liters

    # Calculate the cost of a full tank of diesel fuel
    full_tank_cost = fuel_price_per_liter * tank_capacity
    result = full_tank_cost
    return result

print(solution())