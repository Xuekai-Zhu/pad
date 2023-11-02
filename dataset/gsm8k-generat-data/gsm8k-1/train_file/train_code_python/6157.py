def solution():
    """Joseph has a refrigerator, a water heater in his house, and an electric oven that consumes power at different rates. The total amount of money that Joseph pays for the energy used by the refrigerator is three times the amount he pays for the power used by the water heater. If the electric oven uses power worth $500 in a month, twice what Joseph pays for the power the water heater uses, calculate the total amount he pays for the power used by these gadgets."""
    oven_cost = 500
    water_heater_cost = oven_cost / 2
    fridge_cost = water_heater_cost * 3
    total_cost = oven_cost + water_heater_cost + fridge_cost
    result = total_cost
    return result

print(solution())