def solution():
    original_price = 125
    sale_discount = 20
    coupon_amount = 10
    store_discount = 10
    sale_price = original_price * (1 - (sale_discount / 100))
    final_price = sale_price * (1 - (store_discount / 100))
    total_saved = original_price - final_price
    result = total_saved
    return result

print(solution())