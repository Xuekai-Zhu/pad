def solution():
    """James decides to sell 80% of his toys. He bought them for $20 each and sells them for $30 each. If he had 200 toys, how much more money did he have compared to before he bought them?"""
    num_toys = 200
    original_cost = 20
    selling_price = 30
    percent_to_sell = 0.8
    num_sold = num_toys * percent_to_sell
    profit_per_toy = selling_price - original_cost
    total_profit = num_sold * profit_per_toy
    original_total_cost = num_toys * original_cost
    net_profit = total_profit - original_total_cost
    result = net_profit
    return result

print(solution())