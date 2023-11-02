def solution():
    """A food truck only sells grilled cheeses. They source their bread for $3.00 a loaf and each loaf makes 10 sandwiches. They spend $30.00 on different cheeses and condiments per 10 sandwiches. If they sell 10 sandwiches for $7.00 each, what is their net profit?"""
    cost_per_loaf = 3
    sandwiches_per_loaf = 10
    cost_per_10_sandwiches = 30
    price_per_10_sandwiches = 70
    profit_per_10_sandwiches = price_per_10_sandwiches - (cost_per_loaf + cost_per_10_sandwiches)/sandwiches_per_loaf
    net_profit = profit_per_10_sandwiches
    return net_profit

print(solution())