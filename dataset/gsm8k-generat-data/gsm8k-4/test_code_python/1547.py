def solution():
    """John buys bags of popcorn for $4 and sells them for $8. How much profit does he get by selling 30 bags?"""
    # Define the cost and selling price of each bag
    cost_per_bag = 4
    price_per_bag = 8

    # Calculate the profit per bag
    profit_per_bag = price_per_bag - cost_per_bag

    # Calculate the total profit by selling 30 bags
    total_profit = profit_per_bag * 30

    result = total_profit
    return result

print(solution())