def solution():
    """Buffy and Oz went to dinner. They shared an appetizer that cost $9.00. Each of their entrees was $20.00 and they shared a dessert that was $11.00. If they left a 30% tip, what was the entire price of the meal?"""
    appetizer_price = 9
    entree_price = 20
    dessert_price = 11
    subtotal = appetizer_price + 2 * entree_price + dessert_price
    tip_percentage = 0.3
    tip_amount = subtotal * tip_percentage
    total_price = subtotal + tip_amount
    result = total_price
    return result

print(solution())