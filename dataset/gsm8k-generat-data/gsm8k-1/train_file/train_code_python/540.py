def solution():
    """Tonya is buying Christmas gifts for her sisters. She has 2 sisters and wants to spend the exact same amount on each. She buys her younger sister 4 dolls that cost $15 each. She plans to buy lego sets for her older sister. They cost $20 each. How many lego sets does she buy?"""
    younger_sister_cost = 4 * 15
    total_cost = younger_sister_cost * 2
    older_sister_cost = total_cost / 2
    lego_set_cost = 20
    lego_sets = older_sister_cost / lego_set_cost
    result = lego_sets
    return result

print(solution())