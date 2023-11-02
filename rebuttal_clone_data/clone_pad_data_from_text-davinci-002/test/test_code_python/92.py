def solution():
    
    quiche_price = 15
    croissant_price = 3
    biscuit_price = 2
    quiche_quantity = 2
    croissant_quantity = 6
    biscuit_quantity = 6
    order_total = (quiche_price * quiche_quantity) + (croissant_price * croissant_quantity) + (biscuit_price * biscuit_quantity)
    discount_percentage = 10
    discount_amount = (discount_percentage / 100) * order_total
    final_total = order_total - discount_amount
    result = final_total
    return result

print(solution())