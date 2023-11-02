def solution():
    gas_left = 2
    gas_total = 12
    distance_to_supermarket = 5
    distance_to_farm = 6

    # Calculate the total distance traveled
    total_distance = (distance_to_supermarket * 2) + \
                     (distance_to_farm * 2) + 2  # add 2 miles for returning home to get tools

    # Calculate the total amount of gas used
    gas_used = gas_total - gas_left

    # Calculate the rate of gas consumption in miles per gallon
    miles_per_gallon = total_distance / gas_used
    result = miles_per_gallon
    return result

print(solution())