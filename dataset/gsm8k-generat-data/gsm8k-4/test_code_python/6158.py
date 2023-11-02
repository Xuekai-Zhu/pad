def solution():
    """Joseph has a refrigerator, a water heater in his house, and an electric oven that consumes power at different rates. The total amount of money that Joseph pays for the energy used by the refrigerator is three times the amount he pays for the power used by the water heater. If the electric oven uses power worth $500 in a month, twice what Joseph pays for the power the water heater uses, calculate the total amount he pays for the power used by these gadgets."""
    # Define the power usage rates for the refrigerator, water heater, and oven
    refrigerator_rate = 3
    water_heater_rate = 1
    oven_rate = 2

    # Calculate the power usage for the water heater
    water_heater_power = 500 / (2 * water_heater_rate)

    # Calculate the power usage for the refrigerator
    refrigerator_power = water_heater_power * water_heater_rate * refrigerator_rate

    # Calculate the total power usage and cost
    total_power_usage = refrigerator_power + water_heater_power + 500
    total_cost = total_power_usage * 0.15

    # return the result
    result = total_cost
    return result

print(solution())