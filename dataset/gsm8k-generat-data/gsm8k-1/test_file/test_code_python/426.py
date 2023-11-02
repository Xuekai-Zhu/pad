def solution():
    """Charlotte went into the kitchen supply store knowing she wanted a set of pot and pans for $120.00, a set of mixing bowls for $20.00 and 5 separate utensils at $5.00 each. At check out, the clerk told her everything was 20% off. How much was her order?"""
    pot_and_pan_price = 120
    mixing_bowl_price = 20
    utensils_price = 5 * 5
    total_price = pot_and_pan_price + mixing_bowl_price + utensils_price
    discount = total_price * 0.2
    discounted_price = total_price - discount
    result = discounted_price
    return result

print(solution())