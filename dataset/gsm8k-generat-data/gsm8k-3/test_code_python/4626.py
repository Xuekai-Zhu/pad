def solution():
    """The cost of building a certain house in an area is 100,000 more than the construction cost of each of the houses in the area.  But it sells for 1.5 times as much as the other houses, which sell at $320,000 each. How much more profit is made by spending the extra money to build?"""
    # Define the cost and sale price of each house in the area
    COST_PER_HOUSE = 320000
    SALE_PRICE_PER_HOUSE = 1.5 * COST_PER_HOUSE

    # Calculate the cost and sale price of the special house
    SPECIAL_COST = COST_PER_HOUSE + 100000
    SPECIAL_SALE_PRICE = 1.5 * SPECIAL_COST

    # Calculate the profit of each house
    PROFIT_PER_HOUSE = SALE_PRICE_PER_HOUSE - COST_PER_HOUSE
    SPECIAL_PROFIT = SPECIAL_SALE_PRICE - SPECIAL_COST

    # Calculate the extra profit from building the special house
    EXTRA_PROFIT = SPECIAL_PROFIT - PROFIT_PER_HOUSE

    # Display the extra profit
    result = EXTRA_PROFIT
    return result

print(solution())