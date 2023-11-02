def solution():
    """While cultivating a small farm, a farmer spent $50 on corn seeds, $35 on fertilizers and pesticides, and $15 on labor. After a successful harvest, he was able to gather 10 bags of corn. How much should he sell each bag, if he wants to make a profit of 10%?"""
    total_cost = 50 + 35 + 15
    desired_profit = 0.1 * total_cost
    total_profit = total_cost + desired_profit
    bags_of_corn = 10
    price_per_bag = total_profit / bags_of_corn
    result = price_per_bag
    return result

print(solution())