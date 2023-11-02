def solution():
    """Emily went to the store and bought art supplies for $20 and 2 skirts that cost the same amount of money. She spent a total of $50. How much did Emily pay for each of the skirts?"""
    total_spent = 50
    art_supplies_cost = 20
    skirts_cost = (total_spent - art_supplies_cost) / 2
    result = skirts_cost
    return result

print(solution())