def solution():
    """Sarah has a rope that is 20 meters long. Her friend wants to buy the rope for $2 a meter.
    Sarah plans to use the profit to buy a new rope, which at the store costs $1.5 a meter.
    How much money will she have left over after she buys the new rope?"""
    rope_length = 20
    price_per_meter = 2
    selling_price = rope_length * price_per_meter
    new_rope_price = 1.5 * rope_length
    leftover_money = selling_price - new_rope_price
    result = leftover_money
    return result

print(solution())