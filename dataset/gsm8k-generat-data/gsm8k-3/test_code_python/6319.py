def solution():
    """Jean needs to buy 10 new pairs of pants.  A store is running a sale for 20% off.  If the pants normally retail for $45 each how much will she need to pay for all of them after paying a 10% tax?"""
    # Define the original price per pair of pants
    ORIGINAL_PRICE = 45

    # Calculate the sale price per pair of pants
    sale_price = ORIGINAL_PRICE * 0.8

    # Calculate the total cost for 10 pairs of pants at the sale price
    total_cost = sale_price * 10

    # Add 10% tax to the total cost
    total_cost *= 1.1

    # Display the total cost
    result = total_cost
    return result

print(solution())