def solution():
    soda_cost = 21.0
    water_cost = 8.0
    num_soda = 7
    num_water = 4

    # Calculate the total cost of soda
    total_soda_cost = soda_cost * num_soda

    # Calculate the total cost of water
    total_water_cost = water_cost * num_water

    # Calculate the total cost of all items
    total_cost = total_soda_cost + total_water_cost
    result = total_cost
    return result

print(solution())