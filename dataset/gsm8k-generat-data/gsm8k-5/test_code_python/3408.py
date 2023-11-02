def solution():
    old_power_consumption = 800  # John's old computer used 800 watts
    new_power_consumption = old_power_consumption * 1.5  # John's new computer uses 50% more power
    price_increase = 0.25  # The price of electricity went up by 25%
    old_price_per_kwh = 0.12  # John's old price of electricity was 12 cents per kilowatt-hour
    hours_of_use = 50  # John wants to run his computer for 50 hours

    # Calculate the new price of electricity per kilowatt-hour
    new_price_per_kwh = old_price_per_kwh * (1 + price_increase)

    # Calculate the energy used by the old and new computers in kilowatt-hours
    old_energy_used = old_power_consumption * hours_of_use / 1000
    new_energy_used = new_power_consumption * hours_of_use / 1000

    # Calculate the cost of running each computer for 50 hours
    old_cost = old_energy_used * old_price_per_kwh
    new_cost = new_energy_used * new_price_per_kwh

    # Calculate the difference in cost between the old and new computers
    cost_difference = new_cost - old_cost
    result = cost_difference
    return result

print(solution())