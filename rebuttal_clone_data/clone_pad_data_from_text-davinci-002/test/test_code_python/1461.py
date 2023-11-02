def solution():
    base_price = 85
    discount_1 = 20
    discount_2 = 25
    discounted_price_1 = base_price * (1 - (discount_1 / 100))
    discounted_price_2 = discounted_price_1 * (1 - (discount_2 / 100))
    result = discounted_price_2
    return result

print(solution())