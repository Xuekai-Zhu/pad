def solution():
    """The bananas at the supermarket cost $0.80 each, or a bunch for $3.00. Jenny buys 10 bunches that average 4 bananas per bunch. How much money, in dollars, did she save by buying the bananas in bunches instead of individually?"""
    cost_per_banana = 0.8
    cost_per_bunch = 3
    bananas_per_bunch = 4
    total_bananas = 10 * bananas_per_bunch
    individual_cost = total_bananas * cost_per_banana
    bunch_cost = (total_bananas // bananas_per_bunch) * cost_per_bunch
    money_saved = individual_cost - bunch_cost
    result = money_saved
    return result

print(solution())