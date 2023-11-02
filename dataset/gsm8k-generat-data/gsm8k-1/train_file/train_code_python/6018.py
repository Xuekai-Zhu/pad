def solution():
    """Mark buys a Magic card for $100, which then triples in value. How much profit would he make selling it?"""
    purchase_price = 100
    sale_price = purchase_price * 3
    profit = sale_price - purchase_price
    result = profit
    return result

print(solution())