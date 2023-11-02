def solution():
    # Calculate the amount of water in the tank before filling
    initial_water = (1/3) * tank_capacity

    # Calculate the total amount of water in the tank with the added 16 gallons
    total_water = initial_water + 16

    # Calculate the capacity of the tank when full
    full_capacity = total_water / (2/3)
    result = full_capacity
    return result

print(solution())