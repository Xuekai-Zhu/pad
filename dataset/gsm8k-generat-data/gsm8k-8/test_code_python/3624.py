def solution():
    # Define the truck's mileage and distance to the cheaper gas station
    mileage = 3
    distance_to_gas_station = 90

    # Calculate how much gas the truck currently has
    current_gas = 12

    # Calculate how much gas the truck will use on the way to the cheaper gas station
    gas_used = distance_to_gas_station / mileage

    # Subtract the current gas from the total gas needed
    gas_needed = gas_used - current_gas
    result = gas_needed
    return result

print(solution())