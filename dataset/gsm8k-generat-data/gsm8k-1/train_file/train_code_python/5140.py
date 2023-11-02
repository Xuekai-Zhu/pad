def solution():
    """Buffy and Oz went to dinner. They shared an appetizer that cost $9.00. Each of their entrees was $20.00 and they shared a dessert that was $11.00. If they left a 30% tip, what was the entire price of the meal?"""
    appetizer_cost = 9
    entree_cost = 20
    dessert_cost = 11
    subtotal = (appetizer_cost + (2 * entree_cost) + dessert_cost)
    tip_percent = 30
    tip = subtotal * (tip_percent / 100)
    total_cost = subtotal + tip
    result = total_cost
    return result

print(solution())