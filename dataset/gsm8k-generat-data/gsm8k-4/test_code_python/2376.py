def solution():
    """A local restaurant was offering a "Build Your Own Hot Brownie" dessert.  The brownie cost $2.50 and each scoop of ice cream costs $1.00.  Any syrup costs $0.50 and nuts cost $1.50.  If Juanita orders the brownie with 2 scoops of ice cream, double syrup, and nuts, how much will her dessert cost?"""
    # Define the prices
    BROWNIE_PRICE = 2.5
    ICE_CREAM_PRICE = 1.0
    SYRUP_PRICE = 0.5
    NUTS_PRICE = 1.5

    # Calculate the cost of Juanita's dessert
    dessert_cost = BROWNIE_PRICE + (2 * ICE_CREAM_PRICE) + (2 * SYRUP_PRICE) + NUTS_PRICE

    # return the result
    result = dessert_cost
    return result

print(solution())