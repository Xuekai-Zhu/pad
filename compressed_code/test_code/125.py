def solution():
    
    quiche_price = 15
    croissant_price = 3
    biscuit_price = 2
    total_order_price = (2 * quiche_price) + (6 * croissant_price) + (6 * biscuit_price)  
    if total_order_price > 50:  
        total_order_price *= 0.9
    result = total_order_price
    return result

print(solution())