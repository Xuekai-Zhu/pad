def solution():
    # Calculate the total weight of the nails
    nails_weight = 4 * 5

    # Calculate the total weight of the hammers
    hammers_weight = 12 * 5

    # Calculate the maximum weight of the wooden planks that can be loaded
    max_wooden_weight = 20 * 15 - nails_weight - hammers_weight

    # Calculate the weight of the wooden planks
    wooden_weight = 10 * 30

    # Determine how much wooden weight needs to be left out to meet the weight limit
    if wooden_weight > max_wooden_weight:
        left_out_weight = wooden_weight - max_wooden_weight
    else:
        left_out_weight = 0

    result = left_out_weight
    return result

print(solution())