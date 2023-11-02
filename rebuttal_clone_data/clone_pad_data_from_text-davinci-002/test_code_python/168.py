def solution():
    """Silvia’s bakery is offering 10% on advanced orders over $50.00. She orders 2 quiches for $15.00 each, 6 croissants at $3.00 each and 6 buttermilk biscuits for $2.00 each. How much will her order be with the discount?"""
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