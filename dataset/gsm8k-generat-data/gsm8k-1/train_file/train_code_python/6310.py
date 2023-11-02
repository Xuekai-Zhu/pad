def solution():
    """An online website offers a flat rate shipping price of $5.00 if the purchase is below $50.00. If it's above $50.00 then they will charge 20% of the purchase price for shipping. Thomas orders 3 shirts for $12.00 each, a pack of socks for $5.00, 2 pairs of shorts for $15.00 each and a pair of swim trunks for $14.00 How much will his total bill be, including shipping?"""
    shirt_cost = 12.00
    num_shirts = 3
    sock_cost = 5.00
    num_socks = 1
    shorts_cost = 15.00
    num_shorts = 2
    trunks_cost = 14.00
    num_trunks = 1

    subtotal = (shirt_cost * num_shirts) + (sock_cost * num_socks) + (
        shorts_cost * num_shorts) + (trunks_cost * num_trunks)

    if subtotal < 50.00:
        shipping_cost = 5.00
    else:
        shipping_cost = subtotal * 0.20

    total_cost = subtotal + shipping_cost
    result = total_cost
    return result

print(solution())