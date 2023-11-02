def solution():
    num_necklaces = 3
    total_cost = 240000
    earring_cost = 3

    # Calculate the cost of the earrings
    earrings_total_cost = earring_cost * num_necklaces

    # Calculate the total cost of the necklaces
    necklaces_total_cost = total_cost - earrings_total_cost

    # Calculate the cost of a single necklace
    single_necklace_cost = necklaces_total_cost / num_necklaces
    result = single_necklace_cost
    return result

print(solution())