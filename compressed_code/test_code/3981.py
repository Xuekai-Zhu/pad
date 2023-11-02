def solution():
    
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