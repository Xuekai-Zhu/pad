def solution():
    """Bronson is an apple dealer. He buys apples from farmers and then transports them to the grocery stores and sells them for profit. He buys individual apples from farmers at a cost of $12 per bushel, and sells them to the stores at a price of $0.40 per apple. If each bushel contains 48 apples, then how much profit, in dollars, does he make after selling 100 apples?"""
    cost_per_apple = 12 / 48
    selling_price_per_apple = 0.4
    profit_per_apple = selling_price_per_apple - cost_per_apple
    profit = profit_per_apple * 100
    result = profit
    return result

print(solution())