def solution():
    # Define the total cost and the ratios between the prices of the necklaces and the earrings
    total_cost = 240000
    necklace_to_earring_ratio = 1/3

    # Calculate the cost of the earrings
    earring_cost = total_cost * necklace_to_earring_ratio

    # Calculate the cost of one necklace
    necklace_cost = (total_cost - earring_cost) / 3

    result = necklace_cost
    return result

print(solution())