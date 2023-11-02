def solution():
    num_days = 2  # Tara is driving for two days
    num_fills = 2  # Tara stops to fill up her tank twice
    num_gas_stations = 4  # Tara visits 4 gas stations in total
    gas_prices = [3, 3.5, 4, 4.5]  # Tara encounters gas prices of $3, $3.50, $4, and $4.50 per gallon
    tank_size = 12 # Tara's car has a 12-gallon tank

    # Calculate the total amount of gas used
    total_gas_used = tank_size * num_fills

    # Calculate the total cost of gas for the trip
    total_cost = 0
    for i in range(num_gas_stations):
        # Calculate the cost of filling up the tank at each gas station
        gas_cost = gas_prices[i] * tank_size

        # Add the cost to the total cost of the trip
        total_cost += gas_cost

    result = total_cost
    return result

print(solution())