def solution():
    """The pet store can buy a goldfish for $.25 and sell it for $.75. The owner plans to use the profits from goldfish sales to buy a new tank, which costs $100. After one week, he is 45% short of the price. How many goldfish did he sell that week?"""
    cost_per_fish = 0.25
    sale_per_fish = 0.75
    profit_per_fish = sale_per_fish - cost_per_fish
    tank_price = 100
    profit_needed = tank_price * 0.45
    fish_needed = profit_needed / profit_per_fish
    fish_sold = round(fish_needed)
    result = fish_sold
    return result

print(solution())