def solution():
    """Enrique earns a 15% commission on every piece of clothing item he sells. In one day he sells 2 $700.00 suits, 6 shirts that cost $50.00 each, and 2 pairs of loafers that are $150.00 each. How much commission does Enrique earn?"""
    suit_price = 700
    shirt_price = 50
    loafers_price = 150
    total_suit_price = 2 * suit_price
    total_shirt_price = 6 * shirt_price
    total_loafers_price = 2 * loafers_price
    total_sales_price = total_suit_price + total_shirt_price + total_loafers_price
    commission_rate = 0.15
    commission_amount = commission_rate * total_sales_price
    result = commission_amount
    return result

print(solution())