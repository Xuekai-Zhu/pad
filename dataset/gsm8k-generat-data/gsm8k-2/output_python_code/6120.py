def solution():
    """Carrie wants to take a trip to New York. She can get a 20% discount on an $850 flight with Delta Airlines. She can also save 30% off an $1100 flight with United Airlines. How much money would she save by choosing the cheapest flight?"""
    delta_price = 850
    delta_discount = 0.2
    delta_price_with_discount = delta_price * (1 - delta_discount)

    united_price = 1100
    united_discount = 0.3
    united_price_with_discount = united_price * (1 - united_discount)

    if delta_price_with_discount < united_price_with_discount:
        savings = united_price - delta_price_with_discount
    else:
        savings = united_price_with_discount - delta_price

    result = savings
    return result

print(solution())