def solution():
    num_popsicles = 20
    popsicle_price = 0.25

    num_ice_cream_bars = 4
    ice_cream_price = 0.5

    # Calculate the total cost of all popsicles
    total_popsicle_cost = num_popsicles * popsicle_price

    # Calculate the total cost of all ice cream bars
    total_ice_cream_cost = num_ice_cream_bars * ice_cream_price

    # Calculate the total cost of all items
    total_cost = total_popsicle_cost + total_ice_cream_cost
    result = total_cost
    return result

print(solution())