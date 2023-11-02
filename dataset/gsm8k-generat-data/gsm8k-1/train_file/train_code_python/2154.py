def solution():
    """Tilly needs to sell 100 bags at $10 per bag to make $300 in profit. How much did she buy each bag for?"""
    bags_to_sell = 100
    selling_price_per_bag = 10
    desired_profit = 300
    cost_per_bag = (bags_to_sell * selling_price_per_bag - desired_profit) / bags_to_sell
    result = cost_per_bag
    return result

print(solution())