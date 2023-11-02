def solution():
    # Calculate the total amount of ice needed for the BBQ
    total_ice = 15 * 2  # 2 pounds of ice per person, for 15 people

    # Calculate the number of ice packs needed
    num_ice_packs = total_ice / 10  # each pack contains 10 one-pound bags of ice

    # Calculate the total cost of the ice
    ice_cost = num_ice_packs * 3.00  # each pack costs $3.00

    result = ice_cost
    return result

print(solution())