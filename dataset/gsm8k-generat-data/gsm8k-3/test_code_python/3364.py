def solution():
    """Zane purchases 2 polo shirts from the 40% off rack at the men’s store.  The polo shirts are $50 each at the regular price.  How much did he pay for the shirts?"""
    # Define the regular price of the polo shirt
    REGULAR_PRICE = 50

    # Calculate the sale price of the polo shirt
    sale_price = REGULAR_PRICE * 0.6

    # Calculate the total cost of the two polo shirts
    total_cost = sale_price * 2

    # Display the total cost
    result = total_cost
    return result

print(solution())