def solution():
    """Bronson is an apple dealer. He buys apples from farmers and then transports them to the grocery stores and sells them for profit. He buys individual apples from farmers at a cost of $12 per bushel, and sells them to the stores at a price of $0.40 per apple. If each bushel contains 48 apples, then how much profit, in dollars, does he make after selling 100 apples?"""
    # Define the cost per bushel and the number of apples per bushel
    COST_PER_BUSHEL = 12
    APPLES_PER_BUSHEL = 48

    # Calculate the cost per apple
    cost_per_apple = COST_PER_BUSHEL / APPLES_PER_BUSHEL

    # Calculate the revenue from selling 100 apples
    revenue = 100 * 0.4

    # Calculate the cost of buying 100 apples
    cost = 100 * cost_per_apple

    # Calculate the profit
    profit = revenue - cost

    # return the result
    result = profit
    return result

print(solution())