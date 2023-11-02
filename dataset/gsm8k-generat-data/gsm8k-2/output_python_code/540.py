def solution():
    """Tonya is buying Christmas gifts for her sisters. She has 2 sisters and wants to spend the exact same amount on each. She buys her younger sister 4 dolls that cost $15 each. She plans to buy lego sets for her older sister. They cost $20 each. How many lego sets does she buy?"""
    younger_sister_gift_cost = 4 * 15
    older_sister_gift_cost = younger_sister_gift_cost
    lego_set_cost = 20
    num_lego_sets = older_sister_gift_cost / lego_set_cost
    result = num_lego_sets
    return result

print(solution())