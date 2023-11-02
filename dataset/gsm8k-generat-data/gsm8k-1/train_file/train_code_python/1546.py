def solution():
    """John buys bags of popcorn for $4 and sells them for $8. How much profit does he get by selling 30 bags?"""
    buy_price = 4
    sell_price = 8
    num_bags = 30
    cost = buy_price * num_bags
    revenue = sell_price * num_bags
    profit = revenue - cost
    result = profit
    return result

print(solution())