def solution():
    """Linda makes and sells necklaces at craft fairs. At her most recent fair she sold 4 necklaces and 8 rings for a total of $80. If each necklace costs $12, how much does each ring cost?"""
    # Define the number of necklaces sold and their price
    necklaces_sold = 4
    necklace_price = 12

    # Calculate the total revenue from necklaces
    necklace_revenue = necklaces_sold * necklace_price

    # Calculate the revenue from rings
    ring_revenue = 80 - necklace_revenue

    # Calculate the price of each ring
    rings_sold = 8
    ring_price = ring_revenue / rings_sold

    result = ring_price
    return result

print(solution())