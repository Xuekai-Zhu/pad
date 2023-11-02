def solution():
    """A retailer sells any shirt for the same price and any pair of pants for the same price, but the price of shirts and pants are not the same. Say you bought 2 shirts and 3 pairs of pants for $120 in total, then you realized you didn't need the extra pants. What's the price of 1 shirt at this place if when you returned all 3 pairs of pants you were refunded 25% of what you originally paid?"""
    total_cost = 120
    num_shirts = 2
    num_pants = 3
    refund_percent = 0.25
    pants_price = (total_cost / (num_shirts + num_pants)) * (1 - refund_percent)
    shirt_price = (total_cost - (num_pants * pants_price)) / num_shirts
    result = shirt_price
    return result

print(solution())