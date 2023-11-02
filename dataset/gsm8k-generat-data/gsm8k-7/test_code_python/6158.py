def solution():
    oven_cost = 500
    water_heater_cost = oven_cost / 2
    fridge_cost = water_heater_cost * 3

    # Calculate the total cost of power used by all gadgets
    total_cost = oven_cost + water_heater_cost + fridge_cost
    result = total_cost
    return result

print(solution())