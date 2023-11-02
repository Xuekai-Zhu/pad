def solution():
    # Define the variables
    gas_tank = 12
    distance_to_work = 10
    remaining_gas = gas_tank - (2/3 * gas_tank)
    total_distance = 2 * distance_to_work

    # Calculate the miles per gallon
    miles_per_gallon = total_distance / remaining_gas
    result = miles_per_gallon
    return result

print(solution())