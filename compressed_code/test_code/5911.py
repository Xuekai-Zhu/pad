def solution():
    
    quiche_price = 15
    croissant_price = 3
    biscuit_price = 2
    total_order = (2 * quiche_price) + (6 * croissant_price) + (6 * biscuit_price)
    
    if total_order > 50:
        discount = total_order * 0.1
        total_order -= discount
    
    result = total_order
    return result

print(solution())