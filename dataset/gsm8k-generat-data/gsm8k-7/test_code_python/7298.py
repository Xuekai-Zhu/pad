def solution():
    initial_gas = 47
    final_gas = 14
    distance = 275

    # Calculate the amount of gas used during the journey
    gas_used = initial_gas - final_gas

    # Calculate the fuel consumption per kilometer
    fuel_consumption = gas_used / distance

    # Calculate the fuel consumption per 100 km
    fuel_consumption_100km = fuel_consumption * 100
    result = fuel_consumption_100km
    return result

print(solution())