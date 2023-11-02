def solution():
    """Emily went to the store and bought art supplies for $20 and 2 skirts that cost the same amount of money. She spent a total of $50. How much did Emily pay for each of the skirts?"""
    total_spent = 50
    art_supplies_cost = 20
    skirt_count = 2
    total_skirt_cost = total_spent - art_supplies_cost
    cost_per_skirt = total_skirt_cost / skirt_count
    result = cost_per_skirt
    return result

print(solution())