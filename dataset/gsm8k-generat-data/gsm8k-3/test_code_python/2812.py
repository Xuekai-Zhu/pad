def solution():
    """A magazine costs $3 each. Jewel bought 10 magazines to be sold at $3.50 each. How much will be Jewel gain from selling these?"""
    # Define the cost and selling price of each magazine
    COST = 3
    SELL_PRICE = 3.5

    # Define the number of magazines purchased
    magazines_purchased = 10

    # Calculate the profit from selling the magazines
    profit = (SELL_PRICE - COST) * magazines_purchased

    # Display the profit
    result = profit
    return result

print(solution())