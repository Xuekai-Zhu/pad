def solution():
    """Bronson is an apple dealer.  He buys apples from farmers and then transports them to the grocery stores and sells them for profit.  He buys individual apples from farmers at a cost of $12 per bushel, and sells them to the stores at a price of $0.40 per apple.  If each bushel contains 48 apples, then how much profit, in dollars, does he make after selling 100 apples?"""
    # Define the cost of each bushel and the selling price of each apple
    BUSH_PRICE = 12
    APPLE_PRICE = 0.4

    # Calculate the number of bushels needed to sell 100 apples
    bushels = 100 / 48

    # Calculate the cost of the bushels and the revenue from selling the apples
    cost = bushels * BUSH_PRICE
    revenue = 100 * APPLE_PRICE

    # Calculate the profit
    profit = revenue - cost

    # Display the profit
    result = profit
    return result

print(solution())