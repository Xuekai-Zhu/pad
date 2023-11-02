def solution():
    original_price = 1200
    price_increase = 1200 * 0.1
    price_decrease = price_increase * 0.15
    final_price = original_price + price_increase - price_decrease
    result = original_price - final_price
    return result

print(solution())