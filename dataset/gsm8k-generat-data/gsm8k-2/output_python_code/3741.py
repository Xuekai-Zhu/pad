def solution():
    """A retailer sells any shirt for the same price and any pair of pants for the same price, but the price of shirts and pants are not the same. Say you bought 2 shirts and 3 pairs of pants for $120 in total, then you realized you didn't need the extra pants. What's the price of 1 shirt at this place if when you returned all 3 pairs of pants you were refunded 25% of what you originally paid?"""
    total_items = 5
    total_price = 120
    pants_price = 0
    for i in range(total_items):
        if i < 2:
            total_price -= pants_price
        else:
            pants_price = total_price / 3
            total_price -= pants_price

    refunded_amount = total_price * 0.25
    total_price -= refunded_amount
    shirt_price = total_price / 2
    result = shirt_price
    return result

print(solution())