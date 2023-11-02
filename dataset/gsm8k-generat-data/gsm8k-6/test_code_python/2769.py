def solution():
    # Calculate the total cost of necklaces sold and the remaining cost for rings
    necklaces_cost = 4 * 12  # each necklace costs $12
    rings_remaining_cost = 80 - necklaces_cost  # total cost - necklaces cost

    # Calculate the cost of each ring
    cost_per_ring = rings_remaining_cost / 8
    result = cost_per_ring
    return result

print(solution())