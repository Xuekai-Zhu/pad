def solution():
    original_price = 500
    price_after_1_week = original_price - (original_price * 5 / 100)
    price_after_1_month = price_after_1_week - (price_after_1_week * 4 / 100)
    total_reduction = original_price - price_after_1_month
    result = total_reduction
    return result

print(solution())