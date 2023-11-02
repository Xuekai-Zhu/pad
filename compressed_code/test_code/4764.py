def solution():
    
    oven_power_cost = 500
    water_heater_power_cost = oven_power_cost / 2
    fridge_power_cost = water_heater_power_cost * 3
    total_power_cost = oven_power_cost + water_heater_power_cost + fridge_power_cost
    result = total_power_cost
    return result

print(solution())