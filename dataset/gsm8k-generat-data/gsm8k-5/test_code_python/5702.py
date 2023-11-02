def solution():
    total_fuel = 150  # Donny's truck can hold 150 liters of fuel
    fuel_in_tank = 38  # Donny's truck already has 38 liters of fuel
    fuel_needed = total_fuel - fuel_in_tank  # Donny needs to buy this much fuel

    # Calculate the cost of the fuel Donny needs
    fuel_cost = fuel_needed * 3

    # Calculate how much change Donny will get from $350
    change = 350 - fuel_cost
    result = change
    return result

print(solution())