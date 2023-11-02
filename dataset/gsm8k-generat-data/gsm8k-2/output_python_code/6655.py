def solution():
    """The pet store can buy a goldfish for $.25 and sell it for $.75. The owner plans to use the profits from goldfish sales to buy a new tank, which costs $100. After one week, he is 45% short of the price. How many goldfish did he sell that week?"""
    cost_price = 0.25
    selling_price = 0.75
    profit_per_fish = selling_price - cost_price
    tank_price = 100
    required_profit = 0.55 * tank_price
    num_fish = required_profit / profit_per_fish
    result = num_fish
    return result

print(solution())