def solution():
    oven_cost = 500  # Cost of power used by the electric oven in a month
    water_heater_cost = oven_cost / 2  # Joseph pays half the cost of power used by the electric oven for the water heater
    fridge_cost = 3 * water_heater_cost  # Joseph pays three times the cost of power used by the water heater for the fridge

    # Calculate the total amount Joseph pays for power used by all gadgets
    total_cost = oven_cost + water_heater_cost + fridge_cost
    result = total_cost
    return result

print(solution())