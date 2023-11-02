def solution():
    """Kelly is grocery shopping at a supermarket and is making sure she has enough in her budget for the items in her cart. Her 5 packs of bacon cost $10 in total and she has 6 packets of chicken which each cost twice as much as a pack of bacon. She also has 3 packs of strawberries, priced at $4 each, and 7 packs of apples, each priced at half the price of a pack of strawberries. If Kelly’s budget is $65 then how much money, in dollars, does she have left in her budget?"""
    bacon_cost = 10
    chicken_cost = 2 * bacon_cost
    chicken_count = 6
    strawberries_cost = 4
    strawberries_count = 3
    apples_cost = strawberries_cost / 2
    apples_count = 7
    total_cost = bacon_cost + (chicken_cost * chicken_count) + (strawberries_cost * strawberries_count) + (apples_cost * apples_count)
    remaining_budget = 65 - total_cost
    result = remaining_budget
    return result

print(solution())