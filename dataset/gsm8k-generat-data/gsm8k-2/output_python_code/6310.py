def solution():
    """An online website offers a flat rate shipping price of $5.00 if the purchase is below $50.00.
    If it's above $50.00 then they will charge 20% of the purchase price for shipping.
    Thomas orders 3 shirts for $12.00 each, a pack of socks for $5.00,
    2 pairs of shorts for $15.00 each and a pair of swim trunks for $14.00.How much will his total bill be, including shipping?"""
    shirts_price = 12
    socks_price = 5
    shorts_price = 15
    swim_trunks_price = 14
    total_purchase_price = (3 * shirts_price) + socks_price + (2 * shorts_price) + swim_trunks_price
    if total_purchase_price < 50:
        shipping_price = 5
    else:
        shipping_price = 0.2 * total_purchase_price
    total_price = total_purchase_price + shipping_price
    result = total_price
    return result

print(solution())