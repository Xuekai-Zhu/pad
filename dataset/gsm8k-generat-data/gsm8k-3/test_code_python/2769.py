def solution():
    """Linda makes and sells necklaces at craft fairs. At her most recent fair she sold 4 necklaces and 8 rings for a total of $80. If each necklace costs $12, how much does each ring cost?"""
    # Define the cost of each necklace
    NECKLACE_COST = 12

    # Calculate the total revenue from necklace sales
    necklace_revenue = 4 * NECKLACE_COST

    # Calculate the total revenue from ring sales
    ring_revenue = 80 - necklace_revenue

    # Calculate the cost of each ring
    ring_cost = ring_revenue / 8

    # Display the cost of each ring
    result = ring_cost
    return result

print(solution())