def solution():
    """Trinity sells magazines at 11/8 of the price she bought the magazines. If she bought the magazines at $72, what is her profit?"""
    buy_price = 72
    sell_price = buy_price * (11/8)
    profit = sell_price - buy_price
    result = profit
    return result

print(solution())