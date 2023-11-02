def solution():
    original_price = 500
    discount_1 = 0.05 # 5% discount
    discount_2 = 0.04 # 4% discount
    new_price_1 = original_price * (1 - discount_1)
    new_price_2 = new_price_1 * (1 - discount_2)
    reduction = original_price - new_price_2
    result = reduction
    return result

print(solution())