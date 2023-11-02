def solution():
    """Mrs. Oaklyn buys handmade rugs at $40 each and sells them at $60 each. If she bought 20 rugs, calculate the profit she will make from selling the rugs."""
    buying_price = 40
    selling_price = 60
    quantity = 20
    revenue = selling_price * quantity
    cost = buying_price * quantity
    profit = revenue - cost
    result = profit
    return result

print(solution())