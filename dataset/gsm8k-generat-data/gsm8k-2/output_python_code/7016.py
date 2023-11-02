def solution():
    """Mrs. Oaklyn buys handmade rugs at $40 each and sells them at $60 each. If she bought 20 rugs, calculate the profit she will make from selling the rugs."""
    buy_price = 40
    sell_price = 60
    num_rugs = 20
    revenue = sell_price * num_rugs
    cost = buy_price * num_rugs
    profit = revenue - cost
    result = profit
    return result

print(solution())