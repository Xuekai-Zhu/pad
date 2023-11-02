def solution():
    """While cultivating a small farm, a farmer spent $50 on corn seeds, $35 on fertilizers and pesticides, and $15 on labor. After a successful harvest, he was able to gather 10 bags of corn. How much should he sell each bag, if he wants to make a profit of 10%?"""
    total_cost = 50 + 35 + 15
    bags = 10
    cost_per_bag = total_cost / bags
    profit_percent = 10
    selling_price_per_bag = cost_per_bag * (1 + (profit_percent / 100))
    result = selling_price_per_bag
    return result

print(solution())