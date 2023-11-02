def solution():
    num_sandwiches = 3
    sandwich_price = 3
    water_price = 2

    # Calculate the total cost of all sandwiches
    total_sandwich_cost = num_sandwiches * sandwich_price

    # Calculate the total cost of the water
    total_water_cost = water_price

    # Calculate the total cost of all shopping items
    total_cost = total_sandwich_cost + total_water_cost
    result = total_cost
    return result

print(solution())