def solution():
    """Rory orders 2 subs for $7.50 each, 2 bags of chips for $1.50 each and 2 cookies for $1.00 each for delivery. There’s a 20% delivery fee added at check out and she wants to add a $5.00 tip. What will her delivery order cost?"""
    subs_cost = 7.5 * 2
    chips_cost = 1.5 * 2
    cookies_cost = 1 * 2
    subtotal = subs_cost + chips_cost + cookies_cost
    delivery_fee = subtotal * 0.2
    tip = 5.0
    total_cost = subtotal + delivery_fee + tip
    result = total_cost
    return result

print(solution())