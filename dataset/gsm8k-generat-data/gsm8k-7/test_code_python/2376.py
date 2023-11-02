def solution():
    brownie_cost = 2.5
    ice_cream_scoop_cost = 1.0
    syrup_cost = 0.5
    nuts_cost = 1.5

    num_ice_cream_scoops = 2
    num_syrups = 2
    num_nuts = 1

    # Calculate the cost of the ice cream scoops
    ice_cream_cost = num_ice_cream_scoops * ice_cream_scoop_cost

    # Calculate the cost of the syrups
    syrup_total_cost = num_syrups * syrup_cost

    # Calculate the cost of the nuts
    nuts_total_cost = num_nuts * nuts_cost

    # Calculate the total cost of the dessert
    total_cost = brownie_cost + ice_cream_cost + syrup_total_cost + nuts_total_cost
    result = total_cost
    return result

print(solution())