def solution():
    """Bruce buys 5 packs of crayons at $5 each, 10 books at $5 each, and 3 calculators at $5 each. If he has $200, how many bags can he buy with the change if one costs $10 each?"""
    total_cost = 5*5 + 10*5 + 3*5
    change = 200 - total_cost
    bags = change // 10
    result = bags
    return result

print(solution())