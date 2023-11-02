def solution():
    """Bobby needed to make some trips with his truck and had only 12 gallons of gasoline. He drives to a supermarket 5 miles away and then drives back home. Then he headed to his farm which was 6 miles away. Two miles into the journey, he turned around and drove back home to retrieve some farming tools he forgot to take earlier and drove down to the farm. If he now has exactly 2 gallons of gasoline left, at what rate in miles per gallon has his truck been consuming gasoline?"""
    
    # Define the initial amount of gas and the distances traveled by Bobby
    initial_gas = 12
    distance_to_supermarket = 10
    distance_to_farm = 14

    # Calculate the gas used during the trips to the supermarket and back
    gas_used_to_supermarket = distance_to_supermarket / (8 * 2)
    
    # Calculate the gas used during the trip to the farm and back (excluding the detour)
    gas_used_to_farm = (distance_to_farm - 2) / (8 * 2)

    # Calculate the gas used during the detour
    gas_used_for_detour = 2 / (8 * 2)

    # Calculate the total gas used
    total_gas_used = gas_used_to_supermarket * 2 + gas_used_to_farm * 2 + gas_used_for_detour

    # Calculate the gas remaining
    gas_remaining = initial_gas - total_gas_used

    # Calculate the rate of gas consumption in miles per gallon
    rate = distance_to_supermarket / gas_used_to_supermarket + (distance_to_farm - 2) / gas_used_to_farm + 2 / gas_used_for_detour
    rate = (distance_to_supermarket + distance_to_farm * 2 - 4) / (initial_gas - gas_remaining)

    result = rate
    return result

print(solution())