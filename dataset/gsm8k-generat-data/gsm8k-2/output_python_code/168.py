def solution():
    """Silvia’s bakery is offering 10% on advanced orders over $50.00. She orders 2 quiches for $15.00 each, 6 croissants at $3.00 each and 6 buttermilk biscuits for $2.00 each. How much will her order be with the discount?"""
    quiche_price = 15
    croissant_price = 3
    biscuit_price = 2
    total_order_price = (2 * quiche_price) + (6 * croissant_price) + (6 * biscuit_price)  # calculate total order price before discount
    if total_order_price > 50:  # apply discount if applicable
        total_order_price *= 0.9
    result = total_order_price
    return result

print(solution())