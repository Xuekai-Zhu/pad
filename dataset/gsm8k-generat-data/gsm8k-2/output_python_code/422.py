def solution():
    """Mom went shopping at the market. She left with €55. She bought 2 packs of bananas for €4 each, pears for €2, asparagus for €6 and finally a chicken for €11. How much money does Mom have left?"""
    total_cost = 4 * 2 + 2 + 6 + 11
    remaining_money = 55 - total_cost
    result = remaining_money
    return result

print(solution())