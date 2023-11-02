def solution():
    """Carly is overnight shipping some fresh-baked cookies to her grandma. The shipping cost is equal to a flat $5.00 fee plus $0.80 per pound of weight. If the package weighs 5 pounds, how much does Carly pay for shipping?"""
    flat_fee = 5.00
    weight = 5
    price_per_pound = 0.80
    total_shipping_cost = flat_fee + (weight * price_per_pound)
    result = total_shipping_cost
    return result

print(solution())