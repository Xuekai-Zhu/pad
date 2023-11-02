def solution():
    original_cost = 200  # Original cost to refill the tank
    fuel_capacity = 1  # James initially had one tank
    new_fuel_capacity = 2  # James got an extra tank to double fuel capacity
    fuel_price_increase = 0.2  # Fuel prices increased by 20%

    # Calculate the new cost to refill the tank
    new_cost = original_cost * (new_fuel_capacity / fuel_capacity) * (1 + fuel_price_increase)
    result = new_cost
    return result

print(solution())