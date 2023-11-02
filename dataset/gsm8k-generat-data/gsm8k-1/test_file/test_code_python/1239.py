def solution():
    """Archie buys beef jerky that comes 30 sticks to a bag and costs $18.00 per bag. If Archie buys 1 bag while they're $3.00 off a bag, how much will each stick of jerky cost in cents?"""
    sticks_per_bag = 30
    original_price = 18.00
    discount = 3.00
    discounted_price = original_price - discount
    cost_per_stick = discounted_price / sticks_per_bag * 100
    result = cost_per_stick
    return result

print(solution())