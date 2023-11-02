def solution():
    # Define the number of necklaces sold and their individual cost
    num_necklaces = 4
    necklace_cost = 12

    # Calculate the total revenue from necklaces sold
    necklace_revenue = num_necklaces * necklace_cost

    # Calculate the revenue from rings sold
    ring_revenue = 80 - necklace_revenue

    # Calculate the average cost of each ring
    num_rings = 8
    ring_cost = ring_revenue / num_rings
    result = ring_cost
    return result

print(solution())