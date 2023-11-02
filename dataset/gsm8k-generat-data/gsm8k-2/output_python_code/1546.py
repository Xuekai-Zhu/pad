def solution():
    """John buys bags of popcorn for $4 and sells them for $8. How much profit does he get by selling 30 bags?"""
    buy_price = 4
    sell_price = 8
    num_bags = 30
    total_profit = (sell_price - buy_price) * num_bags
    result = total_profit
    return result

print(solution())