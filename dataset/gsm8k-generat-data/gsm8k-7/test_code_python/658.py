def solution():
    original_price_1 = 950
    discount_1 = 0.06  # 6% discount
    price_1 = original_price_1 * (1 - discount_1)

    original_price_2 = 920
    discount_2 = 0.05  # 5% discount
    price_2 = original_price_2 * (1 - discount_2)

    price_difference = abs(price_1 - price_2)
    result = price_difference
    return result

print(solution())