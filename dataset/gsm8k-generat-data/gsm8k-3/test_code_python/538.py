def solution():
    """A luxury bag costs $3000. A reseller wants to get a 15% profit. How much should she sell the bag?"""
    # Define the cost of the bag and the desired profit margin
    COST = 3000
    PROFIT_MARGIN = 0.15

    # Calculate the reseller's desired selling price
    selling_price = COST * (1 + PROFIT_MARGIN)

    # Display the selling price
    result = selling_price
    return result

print(solution())