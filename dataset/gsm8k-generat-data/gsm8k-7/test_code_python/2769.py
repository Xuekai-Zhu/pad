def solution():
    num_necklaces = 4
    necklace_cost = 12

    total_sale = 80

    # Calculate the total cost of all necklaces sold
    total_necklace_cost = num_necklaces * necklace_cost

    # Calculate the total cost of all rings sold
    total_ring_cost = total_sale - total_necklace_cost

    # Calculate the cost of one ring
    ring_cost = total_ring_cost / 8
    result = ring_cost
    return result

print(solution())