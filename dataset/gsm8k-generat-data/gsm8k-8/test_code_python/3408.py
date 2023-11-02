def solution():
    # Define the given values
    old_wattage = 800
    new_wattage = 1.5 * old_wattage
    old_price_per_kWh = 0.12
    hours_used = 50

    # Calculate the new price per kWh
    new_price_per_kWh = old_price_per_kWh * 1.25

    # Calculate the total energy use in kWh
    old_kWh_used = (old_wattage / 1000) * hours_used
    new_kWh_used = (new_wattage / 1000) * hours_used

    # Calculate the cost of running each computer for the specified time
    old_cost = old_kWh_used * old_price_per_kWh
    new_cost = new_kWh_used * new_price_per_kWh

    # Calculate the difference in cost between the two computers
    cost_difference = new_cost - old_cost
    result = cost_difference
    return result

print(solution())