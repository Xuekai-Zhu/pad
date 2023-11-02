def solution():
    """The cost of building a certain house in an area is 100,000 more than the construction cost of each of the houses in the area. But it sells for 1.5 times as much as the other houses, which sell at $320,000 each. How much more profit is made by spending the extra money to build?"""
    construction_cost = 320000
    extra_cost = 100000
    selling_price = 1.5 * construction_cost
    profit_with_extra_cost = selling_price - (construction_cost + extra_cost)
    profit_without_extra_cost = selling_price - construction_cost
    extra_profit = profit_with_extra_cost - profit_without_extra_cost
    result = extra_profit
    return result

print(solution())