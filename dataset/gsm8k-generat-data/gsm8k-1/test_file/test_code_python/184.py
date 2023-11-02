def solution():
    """A trader buys some bags of wheat from a farmer at a rate of $20 per bag. If it costs $2 to transport each bag from the farm to the warehouse, and the trader made a total profit of $400 after selling all the bags at a rate of $30 each, how many bags did he sell?"""
    buy_price = 20
    transport_cost = 2
    sell_price = 30
    total_profit = 400
    net_profit_per_bag = sell_price - buy_price - transport_cost
    num_bags_sold = total_profit / net_profit_per_bag
    result = num_bags_sold
    return result

print(solution())