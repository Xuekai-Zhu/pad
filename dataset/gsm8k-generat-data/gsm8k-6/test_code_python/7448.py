def solution():
    original_price = 120  # original price of the bedside lamp
    discount_rate = 0.20  # 20% discount
    discount_amount = discount_rate * original_price  # amount of discount
    new_price = original_price - discount_amount  # new price after discount
    result = new_price
    return result

print(solution())